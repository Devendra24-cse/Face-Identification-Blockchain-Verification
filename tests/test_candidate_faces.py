from pathlib import Path

import cv2

from search.visual_search import VisualSearch
from search.image_downloader import ImageDownloader
from face.detector import FaceDetector


# --------------------------------------------------
# Project paths
# --------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

input_image = (
    project_root
    / "input"
    / "test.jpg"
)

results_folder = (
    project_root
    / "results"
)

results_folder.mkdir(
    exist_ok=True
)


# --------------------------------------------------
# Initialize components
# --------------------------------------------------

search = VisualSearch()
downloader = ImageDownloader()
detector = FaceDetector()


# --------------------------------------------------
# Google Lens search
# --------------------------------------------------

print("Searching Google Lens...")

results = search.search_image(
    input_image
)

matches = search.get_visual_matches(
    results
)

print(
    f"Found {len(matches)} visual matches."
)


# --------------------------------------------------
# Process candidates
# --------------------------------------------------

MAX_CANDIDATES = 10

processed = 0
faces_found = 0


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
            "❌ No thumbnail available"
        )

        continue


    # --------------------------------------------------
    # Download candidate image
    # --------------------------------------------------

    try:

        print("Downloading image...")

        image = downloader.download(
            thumbnail_url
        )

        print(
            "✓ Download successful"
        )

    except Exception as error:

        print(
            "❌ Download failed:",
            error
        )

        continue


    processed += 1


    # --------------------------------------------------
    # Detect faces
    # --------------------------------------------------

    try:

        detected_faces = detector.detect(
            image
        )

        face_count = len(
            detected_faces
        )

        print(
            f"Faces detected: {face_count}"
        )


    except Exception as error:

        print(
            "❌ Face detection failed:",
            error
        )

        continue


    # --------------------------------------------------
    # Save candidate image
    # --------------------------------------------------

    output_path = (
        results_folder
        / f"candidate_{index}.jpg"
    )

    cv2.imwrite(
        str(output_path),
        image
    )


    # --------------------------------------------------
    # Result
    # --------------------------------------------------

    if face_count > 0:

        faces_found += 1

        print(
            "✓ Face found"
        )

        print(
            "Saved:",
            output_path
        )

    else:

        print(
            "⚠ No face found"
        )


# --------------------------------------------------
# Final summary
# --------------------------------------------------

print("\n\n================================")
print("          FINAL SUMMARY")
print("================================")

print(
    "Candidates requested:",
    min(
        MAX_CANDIDATES,
        len(matches)
    )
)

print(
    "Images processed:",
    processed
)

print(
    "Images with faces:",
    faces_found
)

print(
    "Images without faces:",
    processed - faces_found
)