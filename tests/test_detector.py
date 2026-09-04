from pathlib import Path
import cv2

from face.detector import FaceDetector


# Find project root
project_root = Path(__file__).resolve().parent.parent

# Image we want to test
image_path = project_root / "input" / "test.jpg"

print("Loading image...")

image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(
        f"Could not load image: {image_path}"
    )

print("✓ Image loaded")

print("\nLoading face detector...")

detector = FaceDetector()

print("✓ YuNet loaded")

print("\nDetecting faces...")

faces = detector.detect(image)

print(f"✓ Faces detected: {len(faces)}")

for index, face in enumerate(faces, start=1):
    x, y, width, height = face[:4]
    confidence = face[-1]

    print(f"\nFace {index}")
    print(f"  Position : ({int(x)}, {int(y)})")
    print(f"  Size     : {int(width)} x {int(height)}")
    print(f"  Confidence: {confidence:.4f}")