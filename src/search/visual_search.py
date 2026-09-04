import os
from pathlib import Path

import serpapi
from dotenv import load_dotenv


class VisualSearch:
    def __init__(self):
        # Load variables from .env
        load_dotenv()

        api_key = os.getenv("SERPAPI_KEY")

        if not api_key:
            raise ValueError(
                "SERPAPI_KEY not found in .env"
            )

        self.client = serpapi.Client(
            api_key=api_key
        )

    def search_image(self, image_path):
        """
        Upload a local image and search it using Google Lens.
        """

        image_path = Path(image_path)

        if not image_path.exists():
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        # Upload local image
        upload = self.client.upload_image(
            str(image_path)
        )

        image_id = upload["image_id"]

        # Search uploaded image
        results = self.client.search({
            "engine": "google_lens",
            "image_id": image_id,
        })

        return results

    def get_visual_matches(self, results):
        """
        Extract visual matches from Google Lens results.
        """

        matches = results.get(
            "visual_matches",
            []
        )

        candidates = []

        for match in matches:
            candidate = {
                "title": match.get("title"),
                "source": match.get("source"),
                "link": match.get("link"),
                "thumbnail": match.get("thumbnail"),
            }

            candidates.append(candidate)

        return candidates

    def get_social_matches(self, results):
        social_sources = {
            "Facebook",
            "Instagram",
            "YouTube",
            "TikTok",
            "X",
            "Pinterest",
        }

        social_matches = []

        # Check normal visual matches
        visual_matches = results.get(
            "visual_matches",
            []
        )

        for match in visual_matches:
            source = match.get("source")

            if source in social_sources:
                social_matches.append({
                    "title": match.get("title"),
                    "source": source,
                    "profile_name": match.get("profile_name"),
                    "link": match.get("link"),
                    "thumbnail": match.get("thumbnail"),
                })

        # Check short videos too
        short_videos = results.get(
            "short_videos",
            []
        )

        for match in short_videos:
            source = match.get("source")

            if source in social_sources:
                social_matches.append({
                    "title": match.get("title"),
                    "source": source,
                    "profile_name": match.get("profile_name"),
                    "link": match.get("link"),
                    "thumbnail": match.get("thumbnail"),
                })

        return social_matches