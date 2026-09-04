from pathlib import Path

import cv2

from face.detector import FaceDetector
from face.encoder import FaceEncoder
from face.comparator import FaceComparator

from search.visual_search import VisualSearch
from search.image_downloader import ImageDownloader
from search.candidate_matcher import CandidateMatcher
from search.social_verifier import SocialVerifier


project_root = Path(__file__).resolve().parent.parent

input_image_path = (
    project_root
    / "input"
    / "test.jpg"
)


# --------------------------------
# Load input image
# --------------------------------

print("Loading input image...")

image = cv2.imread(
    str(input_image_path)
)

if image is None:
    raise ValueError(
        "Could not load input image."
    )


# --------------------------------
# Face components
# --------------------------------

detector = FaceDetector()

encoder = FaceEncoder()

comparator = FaceComparator(
    encoder.recognizer
)


# --------------------------------
# Detect input face
# --------------------------------

print("Detecting input face...")

faces = detector.detect(image)

if faces is None or len(faces) == 0:
    raise ValueError(
        "No face detected in input image."
    )

print(
    f"Input faces detected: {len(faces)}"
)


# --------------------------------
# Encode input face
# --------------------------------

input_embedding = encoder.encode(
    image,
    faces[0]
)

print("Input face encoded.")


# --------------------------------
# Google Lens search
# --------------------------------

print("\nSearching Google Lens...")

visual_search = VisualSearch()

search_results = visual_search.search_image(
    input_image_path
)

visual_candidates = (
    visual_search.get_visual_matches(
        search_results
    )
)

social_matches = (
    visual_search.get_social_matches(
        search_results
    )
)

print(
    f"Visual candidates found: "
    f"{len(visual_candidates)}"
)

print(
    f"Social candidates found: "
    f"{len(social_matches)}"
)


# --------------------------------
# Candidate matching
# --------------------------------

print("\nMatching candidate faces...")

downloader = ImageDownloader()

matcher = CandidateMatcher(
    detector,
    encoder,
    comparator,
    downloader
)

ranked_candidates = matcher.match_candidates(
    input_embedding,
    visual_candidates[:20]
)


# --------------------------------
# Social verification
# --------------------------------

print("\nConnecting social results with face matches...")

verifier = SocialVerifier()

social_candidates = (
    verifier.find_social_candidates(
        ranked_candidates,
        social_matches
    )
)


# --------------------------------
# Display results
# --------------------------------

print("\nSocial candidate ranking:")
print("=" * 80)

if not social_candidates:
    print("No social candidate with a detected face was found.")

else:

    for rank, candidate in enumerate(
        social_candidates,
        start=1
    ):

        print(
            f"\n{rank}. "
            f"{candidate.get('title')}"
        )

        print(
            f"   Platform: "
            f"{candidate.get('source')}"
        )

        print(
            f"   Profile: "
            f"{candidate.get('profile_name')}"
        )

        print(
            f"   Face similarity: "
            f"{candidate.get('similarity'):.4f}"
        )

        print(
            f"   URL: "
            f"{candidate.get('link')}"
        )