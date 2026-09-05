import os

import serpapi
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# Get the API key
api_key = os.getenv("SERPAPI_KEY")


# Make sure the key exists
if not api_key:
    raise RuntimeError(
        "SERPAPI_KEY was not found in .env"
    )


print("✓ API key loaded")
print("✓ API key length:", len(api_key))


# Create SerpApi client
client = serpapi.Client(
    api_key=api_key
)


# Perform a simple test search
print("\nSending test request...")

results = client.search({
    "engine": "google",
    "q": "OpenCV"
})


print("✓ Request successful")

print("\nSearch results received.")

print("Result type:", type(results))

print("\nFirst result:")
print(results.get("organic_results", [])[0])
