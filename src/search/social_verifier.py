class SocialVerifier:
    def __init__(self):
        self.social_sources = {
            "Facebook",
            "Instagram",
            "YouTube",
            "TikTok",
            "X",
            "Pinterest",
        }

    def find_social_candidates(
        self,
        ranked_candidates,
        social_matches
    ):
        social_links = {
            match.get("link"): match
            for match in social_matches
            if match.get("link")
        }

        verified_candidates = []

        for candidate in ranked_candidates:
            link = candidate.get("link")

            if link not in social_links:
                continue

            if not candidate.get("face_detected"):
                continue

            similarity = candidate.get("similarity")

            if similarity is None:
                continue

            social_match = social_links[link]

            verified_candidates.append({
                "title": social_match.get("title"),
                "source": social_match.get("source"),
                "profile_name": social_match.get(
                    "profile_name"
                ),
                "link": link,
                "thumbnail": social_match.get(
                    "thumbnail"
                ),
                "face_detected": True,
                "similarity": similarity,
            })

        verified_candidates.sort(
            key=lambda item: item["similarity"],
            reverse=True
        )

        return verified_candidates