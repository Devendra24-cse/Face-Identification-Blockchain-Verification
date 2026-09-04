from pathlib import Path
import cv2

from face.detector import FaceDetector
from face.encoder import FaceEncoder


# Find project root
project_root = Path(__file__).resolve().parent.parent

# Input image
image_path = project_root / "input" / "test.jpg"


# -------------------------
# Load image
# -------------------------

print("Loading image...")

image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(
        f"Could not load image: {image_path}"
    )

print("✓ Image loaded")


# -------------------------
# Detect face
# -------------------------

print("\nLoading YuNet...")

detector = FaceDetector()

print("✓ YuNet loaded")

print("\nDetecting faces...")

faces = detector.detect(image)

print(f"✓ Faces detected: {len(faces)}")


if len(faces) == 0:
    raise RuntimeError("No face detected.")


# For this test, use the first detected face
face = faces[0]

print("\nUsing first detected face.")


# -------------------------
# Generate embedding
# -------------------------

print("\nLoading SFace...")

encoder = FaceEncoder()

print("✓ SFace loaded")

print("\nGenerating face embedding...")

embedding = encoder.encode(
    image,
    face
)

print("✓ Embedding generated")


# -------------------------
# Display information
# -------------------------

print("\n==============================")
print("FACE EMBEDDING INFORMATION")
print("==============================")

print("Embedding shape:", embedding.shape)
print("Embedding type :", embedding.dtype)

print("\nFirst 10 values:")

print(embedding[0][:10])

print("\n==============================")
print("ENCODING TEST PASSED")
print("==============================")