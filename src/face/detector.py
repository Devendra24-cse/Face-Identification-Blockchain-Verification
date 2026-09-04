from pathlib import Path
import cv2


class FaceDetector:
    def __init__(self):
        # Find the root folder of our project
        project_root = Path(__file__).resolve().parent.parent.parent

        # Location of the YuNet model
        model_path = (
            project_root
            / "models"
            / "yunet"
            / "face_detection_yunet_2026may.onnx"
        )

        # Check that the model exists
        if not model_path.exists():
            raise FileNotFoundError(
                f"YuNet model not found: {model_path}"
            )

        # Create the YuNet face detector
        self.detector = cv2.FaceDetectorYN.create(
            str(model_path),
            "",
            (320, 320)
        )

    def detect(self, image):
        """
        Detect faces in an OpenCV image.

        Returns:
            List of detected faces.
        """

        if image is None:
            raise ValueError("Invalid image.")

        # Get image dimensions
        height, width = image.shape[:2]

        # Tell YuNet the actual image size
        self.detector.setInputSize((width, height))

        # Run face detection
        _, faces = self.detector.detect(image)

        # No faces found
        if faces is None:
            return []

        return faces