import cv2


class FaceComparator:

    def __init__(self, recognizer):
        """
        Receive the SFace recognizer object.
        """
        self.recognizer = recognizer

    def cosine_similarity(self, embedding1, embedding2):
        """
        Compare two face embeddings using cosine similarity.
        """

        score = self.recognizer.match(
            embedding1,
            embedding2,
            cv2.FaceRecognizerSF_FR_COSINE
        )

        return float(score)

    def l2_distance(self, embedding1, embedding2):
        """
        Compare two face embeddings using L2 distance.

        Lower distance means more similar.
        """

        distance = self.recognizer.match(
            embedding1,
            embedding2,
            cv2.FaceRecognizerSF_FR_NORM_L2
        )

        return float(distance)