from pathlib import Path
import cv2


PROJECT_ROOT = Path(__file__).resolve().parent.parent

yunet_path = PROJECT_ROOT / "models" / "yunet" / "face_detection_yunet_2026may.onnx"
sface_path = PROJECT_ROOT / "models" / "sface" / "face_recognition_sface_2021dec.onnx"


print("Checking model files...\n")

print("YuNet exists:", yunet_path.exists())
print("SFace exists:", sface_path.exists())


if not yunet_path.exists():
    raise FileNotFoundError(f"YuNet model not found: {yunet_path}")

if not sface_path.exists():
    raise FileNotFoundError(f"SFace model not found: {sface_path}")


print("\nLoading YuNet...")

detector = cv2.FaceDetectorYN.create(
    str(yunet_path),
    "",
    (320, 320)
)

print("✓ YuNet loaded")


print("\nLoading SFace...")

recognizer = cv2.FaceRecognizerSF.create(
    str(sface_path),
    ""
)

print("✓ SFace loaded")

print("\n================================")
print("MODEL TEST PASSED")
print("================================")