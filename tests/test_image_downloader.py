from pathlib import Path

import cv2

from search.visual_search import VisualSearch
from search.image_downloader import ImageDownloader


project_root = Path(__file__).resolve().parent.parent

image_path = project_root / "input" / "test.jpg"


# Google Lens
search = VisualSearch()

print("Searching Google Lens...")

results = search.search_image(
    image_path
)

matches = search.get_visual_matches(
    results
)

print(
    f"Found {len(matches)} visual matches."
)


# Find first candidate that has a thumbnail
candidate = None

for match in matches:
    if match.get("thumbnail"):
        candidate = match
        break


if candidate is None:
    raise RuntimeError(
        "No candidate image found."
    )


print("\nSelected candidate:")
print("Title:", candidate["title"])
print("Source:", candidate["source"])
print("URL:", candidate["thumbnail"])


# Download candidate image
downloader = ImageDownloader()

print("\nDownloading candidate image...")

image = downloader.download(
    candidate["thumbnail"]
)

print("Download successful!")

print(
    "Image dimensions:",
    image.shape
)


# Save it so we can visually inspect it
output_path = (
    project_root
    / "results"
    / "candidate_test.jpg"
)

cv2.imwrite(
    str(output_path),
    image
)

print(
    "\nSaved candidate image to:"
)

print(output_path)