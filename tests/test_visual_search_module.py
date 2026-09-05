from pathlib import Path

from src.search.visual_search import VisualSearch


# Find project root
project_root = Path(__file__).resolve().parent.parent

# Test image
image_path = project_root / "input" / "test.jpg"


print("Starting visual search...")

search = VisualSearch()

results = search.search_image(
    image_path
)

print("\nGoogle Lens search completed.")


# Extract visual matches
visual_matches = search.get_visual_matches(
    results
)

print(
    f"\nVisual matches found: "
    f"{len(visual_matches)}"
)


for index, match in enumerate(
    visual_matches[:10],
    start=1
):

    print(f"\n--- Candidate {index} ---")

    print(
        "Title:",
        match["title"]
    )

    print(
        "Source:",
        match["source"]
    )

    print(
        "Link:",
        match["link"]
    )


# Extract social matches
social_matches = search.get_social_matches(
    results
)

print(
    f"\n\nSocial matches found: "
    f"{len(social_matches)}"
)


for index, match in enumerate(
    social_matches[:10],
    start=1
):

    print(f"\n--- Social Result {index} ---")

    print(
        "Title:",
        match["title"]
    )

    print(
        "Source:",
        match["source"]
    )

    print(
        "Profile:",
        match["profile_name"]
    )

    print(
        "Link:",
        match["link"]
    )
