from pathlib import Path

import cv2

from src.search.visual_search import VisualSearch
from src.search.image_downloader import ImageDownloader
from src.face.detector import FaceDetector
from src.face.encoder import FaceEncoder
from src.face.comparator import FaceComparator


# --------------------------------------------------
# Project paths
# --------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

input_image_path = (
    project_root
    / "input"
    / "test.jpg"
)


# --------------------------------------------------
# Initialize components
# --------------------------------------------------

search = VisualSearch()
downloader = ImageDownloader()
detector = FaceDetector()
encoder = FaceEncoder()

comparator = FaceComparator(
    encoder.recognizer
)


# --------------------------------------------------
# Encode input face
# --------------------------------------------------

print("Processing input image...")

input_image = cv2.imread(
    str(input_image_path)
)

if input_image is None:
    raise ValueError(
        "Could not load input image."
    )


input_faces = detector.detect(
    input_image
)

if len(input_faces) == 0:
    raise ValueError(
        "No face found in input image."
    )

print(
    f"Input faces detected: "
    f"{len(input_faces)}"
)


# Use first detected face
input_embedding = encoder.encode(
    input_image,
    input_faces[0]
)

print("✓ Input face encoded")


# --------------------------------------------------
# Google Lens search
# --------------------------------------------------

print("\nSearching Google Lens...")

results = search.search_image(
    input_image_path
)

matches = search.get_visual_matches(
    results
)

print(
    f"Found {len(matches)} visual matches."
)


# --------------------------------------------------
# Compare candidates
# --------------------------------------------------

MAX_CANDIDATES = 10

results_list = []


for index, candidate in enumerate(
    matches[:MAX_CANDIDATES],
    start=1
):

    print(
        f"\n========== Candidate {index} =========="
    )

    print(
        "Title:",
        candidate.get("title")
    )

    print(
        "Source:",
        candidate.get("source")
    )


    thumbnail_url = candidate.get(
        "thumbnail"
    )

    if not thumbnail_url:

        print(
            "⚠ No thumbnail"
        )

        continue


    # --------------------------------------------------
    # Download candidate
    # --------------------------------------------------

    try:

        candidate_image = downloader.download(
            thumbnail_url
        )

    except Exception as error:

        print(
            "❌ Download failed:",
            error
        )

        continue


    # --------------------------------------------------
    # Detect candidate faces
    # --------------------------------------------------

    try:

        candidate_faces = detector.detect(
            candidate_image
        )

    except Exception as error:

        print(
            "❌ Face detection failed:",
            error
        )

        continue


    if len(candidate_faces) == 0:

        print(
            "⚠ No face detected"
        )

        continue


    print(
        f"Faces detected: "
        f"{len(candidate_faces)}"
    )


    # --------------------------------------------------
    # Compare every detected face
    # --------------------------------------------------

    best_score = -1.0

    for face_number, face in enumerate(
        candidate_faces,
        start=1
    ):

        try:

            candidate_embedding = encoder.encode(
                candidate_image,
                face
            )

            score = comparator.cosine_similarity(
                input_embedding,
                candidate_embedding
            )

            print(
                f"Face {face_number} "
                f"similarity: {score:.4f}"
            )


            if score > best_score:

                best_score = score


        except Exception as error:

            print(
                f"❌ Encoding failed: {error}"
            )


    if best_score >= 0:

        results_list.append({
            "candidate_number": index,
            "title": candidate.get("title"),
            "source": candidate.get("source"),
            "link": candidate.get("link"),
            "score": best_score
        })


# --------------------------------------------------
# Rank candidates
# --------------------------------------------------

results_list.sort(
    key=lambda item: item["score"],
    reverse=True
)


# --------------------------------------------------
# Final ranking
# --------------------------------------------------

print("\n\n================================")
print("       FACE MATCH RANKING")
print("================================")


for rank, result in enumerate(
    results_list,
    start=1
):

    print(
        f"\nRank {rank}"
    )

    print(
        "Candidate:",
        result["candidate_number"]
    )

    print(
        "Title:",
        result["title"]
    )

    print(
        "Source:",
        result["source"]
    )

    print(
        "Similarity:",
        f"{result['score']:.4f}"
    )

    print(
        "Link:",
        result["link"]
    )
