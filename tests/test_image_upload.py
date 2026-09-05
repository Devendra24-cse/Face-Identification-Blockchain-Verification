import os
from pathlib import Path

import serpapi
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# Create SerpApi client
client = serpapi.Client(
    api_key=os.getenv("SERPAPI_KEY")
)

# Locate our test image
project_root = Path(__file__).resolve().parent.parent
image_path = project_root / "input" / "test.jpg"

print("Image:", image_path)
print("Image exists:", image_path.exists())

# Upload local image to SerpApi
print("\nUploading image...")

upload = client.upload_image(
    str(image_path)
)

print("Upload successful!")
print("Image ID:", upload["image_id"])

# Search the uploaded image using Google Lens
print("\nSearching Google Lens...")

results = client.search({
    "engine": "google_lens",
    "image_id": upload["image_id"],
})

print("\nSearch successful!")
print("Response keys:")
print(results.keys())

# Show whether visual matches were returned
if "visual_matches" in results:
    print("\nVisual matches found:")
    
    for match in results["visual_matches"][:5]:
        print("\nTitle:", match.get("title"))
        print("Link:", match.get("link"))
        print("Source:", match.get("source"))

else:
    print("\nNo visual_matches field found.")

# Check exact matches too
if "exact_matches" in results:
    print("\nExact matches:")
    
    for match in results["exact_matches"][:5]:
        print("\nTitle:", match.get("title"))
        print("Link:", match.get("link"))
