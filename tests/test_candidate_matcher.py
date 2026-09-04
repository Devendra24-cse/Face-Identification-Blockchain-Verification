from pathlib import Path

from face.detector import FaceDetector
from face.encoder import FaceEncoder
from face.comparator import FaceComparator

from search.visual_search import VisualSearch
from search.image_downloader import ImageDownloader
from search.candidate_matcher import CandidateMatcher

import cv2


project_root = Path(__file__).resolve().parent.parent

input_image_path = (
    project_root
    / "input"
    / "test.jpg"
)


print("Loading input image...")

image = cv2.imread(
    str(input_image_path)
)

if image is None:
    raise ValueError("Could not load input image.")


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
# Google Lens
# --------------------------------

print("\nSearching Google Lens...")

visual_search = VisualSearch()

search_results = visual_search.search_image(
    input_image_path
)

candidates = visual_search.get_visual_matches(
    search_results
)

print(
    f"Found {len(candidates)} visual matches."
)


# --------------------------------
# Candidate matcher
# --------------------------------

downloader = ImageDownloader()

matcher = CandidateMatcher(
    detector,
    encoder,
    comparator,
    downloader
)


print("\nMatching candidates...\n")

ranked_candidates = matcher.match_candidates(
    input_embedding,
    candidates[:10]
)


# --------------------------------
# Display results
# --------------------------------

print("Ranking:")
print("-" * 70)

for rank, candidate in enumerate(
    ranked_candidates,
    start=1
):

    similarity = candidate.get(
        "similarity"
    )

    if similarity is None:
        score = "No face"

    else:
        score = f"{similarity:.4f}"

    print(
        f"{rank}. "
        f"{candidate.get('title')} "
        f"→ {score}"
    )