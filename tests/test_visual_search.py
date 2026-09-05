import os
from pathlib import Path

import serpapi
from dotenv import load_dotenv


# --------------------------------
# Load environment variables
# --------------------------------

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

if not api_key:
    raise RuntimeError(
        "SERPAPI_KEY was not found in .env"
    )


# --------------------------------
# Find input image
# --------------------------------

project_root = Path(__file__).resolve().parent.parent

image_path = (
    project_root
    / "input"
    / "test.jpg"
)

if not image_path.exists():
    raise FileNotFoundError(
        f"Image not found: {image_path}"
    )


print("Image:", image_path)
print("✓ Image found")


# --------------------------------
# Create SerpApi client
# --------------------------------

client = serpapi.Client(
    api_key=api_key
)

print("✓ SerpApi client created")


# --------------------------------
# Perform Google Lens search
# --------------------------------

print("\nSending image to Google Lens...")

results = client.search({
    "engine": "google_lens",
    "url": str(image_path)
})


# --------------------------------
# Inspect response
# --------------------------------

print("\n✓ Response received")

print("\nResponse type:")
print(type(results))

print("\nResponse keys:")

if hasattr(results, "keys"):
    print(results.keys())


print("\n==============================")
print("RAW SEARCH RESULT")
print("==============================")

print(results)
