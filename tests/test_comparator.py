from pathlib import Path
import cv2

from src.face.detector import FaceDetector
from src.face.encoder import FaceEncoder
from src.face.comparator import FaceComparator


# -------------------------
# Project paths
# -------------------------

project_root = Path(__file__).resolve().parent.parent

image1_path = project_root / "input" / "test.jpg"
image2_path = project_root / "input" / "test_same.jpg"


# -------------------------
# Load images
# -------------------------

print("Loading images...")

image1 = cv2.imread(str(image1_path))
image2 = cv2.imread(str(image2_path))

if image1 is None:
    raise FileNotFoundError(f"Could not load: {image1_path}")

if image2 is None:
    raise FileNotFoundError(f"Could not load: {image2_path}")

print("✓ Both images loaded")


# -------------------------
# Load models
# -------------------------

print("\nLoading face detector...")

detector = FaceDetector()

print("✓ YuNet loaded")

print("\nLoading face encoder...")

encoder = FaceEncoder()

print("✓ SFace loaded")


# -------------------------
# Function to create embedding
# -------------------------

def get_embedding(image, image_name):

    print(f"\nProcessing {image_name}...")

    faces = detector.detect(image)

    if len(faces) == 0:
        raise RuntimeError(
            f"No face detected in {image_name}"
        )

    if len(faces) > 1:
        print(
            f"Warning: {len(faces)} faces detected "
            f"in {image_name}. Using the first face."
        )

    face = faces[0]

    embedding = encoder.encode(
        image,
        face
    )

    print(f"✓ Embedding generated for {image_name}")

    return embedding


#----------------- --------
# Generate embeddings
# -------------------------

embedding1 = get_embedding(
    image1,
    "test.jpg"
)

embedding2 = get_embedding(
    image2,
    "test_same.jpg"
)


# -------------------------
# Compare
# -------------------------

print("\nComparing faces...")

comparator = FaceComparator(
    encoder.recognizer
)

cosine_score = comparator.cosine_similarity(
    embedding1,
    embedding2
)

l2_distance = comparator.l2_distance(
    embedding1,
    embedding2
)


# -------------------------
# Display results
# -------------------------

print("\n==============================")
print("FACE COMPARISON RESULT")
print("==============================")

print(f"Cosine similarity : {cosine_score:.4f}")
print(f"L2 distance       : {l2_distance:.4f}")

print("==============================")
