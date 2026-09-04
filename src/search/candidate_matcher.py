class CandidateMatcher:
    def __init__(self, detector, encoder, comparator, downloader):
        self.detector = detector
        self.encoder = encoder
        self.comparator = comparator
        self.downloader = downloader

    def match_candidates(self, input_embedding, candidates):
        results = []

        for index, candidate in enumerate(candidates, start=1):

            thumbnail = candidate.get("thumbnail")

            if not thumbnail:
                continue

            try:
                image = self.downloader.download(thumbnail)

                faces = self.detector.detect(image)

                if faces is None or len(faces) == 0:
                    results.append({
                        "candidate_number": index,
                        "title": candidate.get("title"),
                        "source": candidate.get("source"),
                        "link": candidate.get("link"),
                        "thumbnail": thumbnail,
                        "face_detected": False,
                        "similarity": None,
                    })
                    continue

                best_similarity = -1.0

                for face in faces:
                    embedding = self.encoder.encode(
                        image,
                        face
                    )

                    similarity = self.comparator.cosine_similarity(
                        input_embedding,
                        embedding
                    )

                    if similarity > best_similarity:
                        best_similarity = similarity

                results.append({
                    "candidate_number": index,
                    "title": candidate.get("title"),
                    "source": candidate.get("source"),
                    "link": candidate.get("link"),
                    "thumbnail": thumbnail,
                    "face_detected": True,
                    "similarity": best_similarity,
                })

            except Exception as error:
                results.append({
                    "candidate_number": index,
                    "title": candidate.get("title"),
                    "source": candidate.get("source"),
                    "link": candidate.get("link"),
                    "thumbnail": thumbnail,
                    "face_detected": False,
                    "similarity": None,
                    "error": str(error),
                })

        results.sort(
            key=lambda item: (
                item["similarity"]
                if item["similarity"] is not None
                else -1
            ),
            reverse=True
        )

        return results