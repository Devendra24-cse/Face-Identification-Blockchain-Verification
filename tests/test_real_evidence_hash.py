from pathlib import Path

import cv2

from src.face.detector import FaceDetector
from src.face.encoder import FaceEncoder
from src.face.comparator import FaceComparator

from src.search.visual_search import VisualSearch
from src.search.image_downloader import ImageDownloader
from src.search.candidate_matcher import CandidateMatcher
from src.search.social_verifier import SocialVerifier

from src.evidence_hasher import EvidenceHasher

from src.blockchain.recorder import BlockchainRecorder  
from src.blockchain.verifier import BlockchainVerifier


# --------------------------------
# Project paths
# --------------------------------

project_root = Path(__file__).resolve().parent.parent

input_image_path = (
    project_root
    / "input"
    / "test.jpg"
)


# --------------------------------
# Load input image
# --------------------------------

print("Loading input image...")

image = cv2.imread(
    str(input_image_path)
)

if image is None:
    raise ValueError(
        "Could not load input image."
    )


# --------------------------------
# Initialize face components
# --------------------------------

detector = FaceDetector()

encoder = FaceEncoder()

comparator = FaceComparator(
    encoder.recognizer
)


# --------------------------------
# Detect input face
# --------------------------------

print("Detecting input face...")

faces = detector.detect(image)

if faces is None or len(faces) == 0:
    raise ValueError(
        "No face detected in input image."
    )

print(
    f"Input faces detected: {len(faces)}"
)


# --------------------------------
# Encode input face
# --------------------------------

input_embedding = encoder.encode(
    image,
    faces[0]
)

print("Input face encoded.")


# --------------------------------
# Google Lens search
# --------------------------------

print("\nSearching Google Lens...")

visual_search = VisualSearch()

search_results = visual_search.search_image(
    input_image_path
)

visual_candidates = (
    visual_search.get_visual_matches(
        search_results
    )
)

social_matches = (
    visual_search.get_social_matches(
        search_results
    )
)

print(
    f"Visual candidates found: "
    f"{len(visual_candidates)}"
)

print(
    f"Social candidates found: "
    f"{len(social_matches)}"
)


# --------------------------------
# Match candidate faces
# --------------------------------

print("\nMatching candidate faces...")

downloader = ImageDownloader()

matcher = CandidateMatcher(
    detector,
    encoder,
    comparator,
    downloader
)

ranked_candidates = matcher.match_candidates(
    input_embedding,
    visual_candidates[:20]
)


# --------------------------------
# Find social candidates
# --------------------------------

print("\nFinding matching social posts...")

verifier = SocialVerifier()

social_candidates = (
    verifier.find_social_candidates(
        ranked_candidates,
        social_matches
    )
)


if not social_candidates:
    raise ValueError(
        "No social candidate with a detected face was found."
    )


# --------------------------------
# Select best social candidate
# --------------------------------

best_candidate = social_candidates[0]


print("\nBest social candidate:")
print("-" * 70)

print(
    f"Platform: "
    f"{best_candidate.get('source')}"
)

print(
    f"Title: "
    f"{best_candidate.get('title')}"
)

print(
    f"Profile: "
    f"{best_candidate.get('profile_name')}"
)

print(
    f"Similarity: "
    f"{best_candidate.get('similarity'):.4f}"
)

print(
    f"URL: "
    f"{best_candidate.get('link')}"
)


# --------------------------------
# Build evidence
# --------------------------------

evidence = {
    "source": best_candidate.get(
        "source"
    ),

    "title": best_candidate.get(
        "title"
    ),

    "profile_name": best_candidate.get(
        "profile_name"
    ),

    "link": best_candidate.get(
        "link"
    ),

    "similarity": round(
        best_candidate.get("similarity"),
        6
    ),
}


# --------------------------------
# Create fingerprint
# --------------------------------

hasher = EvidenceHasher()

fingerprint = hasher.create_fingerprint(
    evidence
)


print("\nEvidence:")
print("-" * 70)

print(evidence)

print("\nSHA-256 fingerprint:")
print(fingerprint)

print("\nFingerprint length:")
print(len(fingerprint))

# --------------------------------
# Record fingerprint on blockchain
# --------------------------------

print("\nRecording fingerprint on blockchain...")

recorder = BlockchainRecorder()

blockchain_result = recorder.record_fingerprint(
    fingerprint
)

print("\nBlockchain record created:")
print("-" * 70)

print(
    f"Transaction hash: "
    f"{blockchain_result['transaction_hash']}"
)

print(
    f"Block number: "
    f"{blockchain_result['block_number']}"
)

print(
    f"Transaction status: "
    f"{blockchain_result['status']}"
)

print(
    f"Gas used: "
    f"{blockchain_result['gas_used']}"
)

# --------------------------------
# Verify fingerprint on blockchain
# --------------------------------

print("\nVerifying fingerprint on blockchain...")

blockchain_verifier = BlockchainVerifier()

verification_result = (
    blockchain_verifier.verify_fingerprint(
        fingerprint,
        blockchain_result["transaction_hash"]
    )
)


print("\nBlockchain verification:")
print("-" * 70)

print(
    f"Local fingerprint: "
    f"{verification_result['local_fingerprint']}"
)

print(
    f"Blockchain fingerprint: "
    f"{verification_result['blockchain_fingerprint']}"
)


print("\nVerification result:")

if verification_result["match"]:
    print("MATCH")
    print("VERIFIED")
else:
    print("MISMATCH")
    print("NOT VERIFIED")
