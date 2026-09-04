from pathlib import Path

from search.visual_search import VisualSearch


project_root = Path(__file__).resolve().parent.parent

input_image_path = (
    project_root
    / "input"
    / "test.jpg"
)


print("Searching Google Lens...")

visual_search = VisualSearch()

results = visual_search.search_image(
    input_image_path
)

social_matches = visual_search.get_social_matches(
    results
)


print(
    f"\nSocial matches found: "
    f"{len(social_matches)}"
)

print("-" * 70)


for index, match in enumerate(
    social_matches,
    start=1
):

    print(
        f"\n{index}. {match.get('title')}"
    )

    print(
        f"   Source: "
        f"{match.get('source')}"
    )

    print(
        f"   Profile: "
        f"{match.get('profile_name')}"
    )

    print(
        f"   Link: "
        f"{match.get('link')}"
    )