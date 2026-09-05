# Face Identification & Blockchain Verification

A Python-based face identification and evidence verification pipeline that combines **computer vision, visual search, social-media verification, cryptographic hashing, and Ethereum blockchain technology**.

The system takes a face image as input, finds visually related candidates, compares faces, identifies relevant social-media evidence, generates a SHA-256 fingerprint of the selected evidence, and records that fingerprint on the Ethereum Sepolia testnet. The fingerprint can then be retrieved from the blockchain and compared with the local fingerprint to verify its integrity.

---

## Table of Contents

* [Overview](#overview)
* [Project Objective](#project-objective)
* [Key Features](#key-features)
* [System Workflow](#system-workflow)
* [Architecture](#architecture)
* [Project Structure](#project-structure)
* [Core Modules](#core-modules)
* [Technology Stack](#technology-stack)
* [Example Output](#example-output)
* [Advantages](#advantages)
* [Limitations](#limitations)
* [Installation](#installation)
* [Environment Configuration](#environment-configuration)
* [Running the Project](#running-the-project)
* [Testing](#testing)
* [Security](#security)
* [Project Status](#project-status)
* [Future Improvements](#future-improvements)

---

## Overview

The project is designed as an end-to-end verification pipeline:

```text
Input Face Image
       │
       ▼
Face Detection
       │
       ▼
Face Encoding
       │
       ▼
Visual Search
       │
       ▼
Candidate Images
       │
       ▼
Face Similarity Matching
       │
       ▼
Social Media Verification
       │
       ▼
Evidence Object
       │
       ▼
SHA-256 Fingerprint
       │
       ▼
Ethereum Sepolia
       │
       ▼
Blockchain Readback
       │
       ▼
Fingerprint Comparison
       │
       ▼
MATCH / VERIFIED
```

The main idea is to use blockchain as an **integrity layer** rather than storing the complete image or evidence directly on-chain.

---

## Project Objective

The objective of this project is to demonstrate how **face recognition, web-based visual search, evidence generation, cryptographic hashing, and blockchain verification** can be combined into a single system.

The system:

1. Detects a face from an input image.
2. Generates a face embedding.
3. Searches for visually related images.
4. Finds and compares faces in candidate images.
5. Searches for relevant social-media evidence.
6. Selects the strongest matching evidence.
7. Generates a SHA-256 fingerprint.
8. Records the fingerprint on Ethereum Sepolia.
9. Retrieves the fingerprint from the blockchain.
10. Compares both fingerprints.
11. Returns `MATCH` and `VERIFIED` when they are identical.

---

## Key Features

| Feature                 | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| Face Detection          | Detects faces using the YuNet model                                |
| Face Encoding           | Generates face embeddings using SFace                              |
| Visual Search           | Retrieves visually related results through Google Lens via SerpApi |
| Candidate Processing    | Downloads and processes candidate images                           |
| Face Matching           | Compares input and candidate face embeddings                       |
| Candidate Ranking       | Ranks candidates according to similarity                           |
| Social Search           | Finds relevant social-media results                                |
| Social Verification     | Connects social results with matching candidates                   |
| Evidence Generation     | Creates a structured evidence object                               |
| SHA-256 Hashing         | Creates a fixed 64-character evidence fingerprint                  |
| Blockchain Recording    | Stores the fingerprint in an Ethereum Sepolia transaction          |
| Blockchain Verification | Reads the fingerprint back from the blockchain                     |
| Integrity Check         | Compares local and blockchain fingerprints                         |

---

## System Workflow

### 1. Input Image

The system starts with an image containing a face.

```text
input/test.jpg
```

The image is loaded and prepared for face detection.

### 2. Face Detection

YuNet detects faces in the input image and provides the detected face region and confidence.

```text
Input image
     ↓
YuNet
     ↓
Detected face
```

### 3. Face Encoding

The detected face is processed using SFace to generate a numerical face embedding.

This embedding is used for similarity comparison with faces found in candidate images.

### 4. Visual Search

The system performs a visual search using Google Lens through SerpApi.

Example result:

```text
Visual candidates found: 59
```

### 5. Candidate Matching

Candidate images are downloaded and processed individually.

```text
Candidate Image
      ↓
Face Detection
      ↓
Face Encoding
      ↓
Similarity Calculation
```

Candidates with stronger similarity scores are ranked higher.

### 6. Social Verification

The system searches the available results for social-media evidence and compares them with the identified candidate.

Example:

```text
Social candidates found: 20
```

### 7. Evidence Generation

The strongest result is converted into a structured evidence object containing information such as:

* Source platform
* Title
* Profile name, when available
* URL
* Face similarity score

### 8. SHA-256 Fingerprint

The evidence is converted into a deterministic representation and hashed using SHA-256.

Example:

```text
3961d219dbb68f430721ce48354c8201b1cc2711d87d5b809f14c3d7e87f222f
```

The resulting fingerprint contains **64 hexadecimal characters**.

### 9. Blockchain Recording

The fingerprint is recorded in a transaction on the Ethereum Sepolia testnet.

The original evidence does not need to be stored directly on the blockchain.

```text
Evidence
   ↓
SHA-256
   ↓
Fingerprint
   ↓
Ethereum Sepolia
```

### 10. Blockchain Verification

The system retrieves the transaction data and extracts the stored fingerprint.

It then compares:

```text
Local Fingerprint
       │
       ├──── Compare ────┐
       │                 │
Blockchain Fingerprint  │
       │                 │
       └─────────────────┘
```

If both fingerprints are identical:

```text
MATCH
VERIFIED
```

---

## Architecture

The project is organized into independent modules for face processing, search, evidence generation, and blockchain operations.

```text
                         ┌────────────────────┐
                         │    Input Image     │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │   Face Detection   │
                         │       YuNet        │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │   Face Encoding    │
                         │       SFace        │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │    Visual Search   │
                         │ Google Lens/SerpApi│
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Candidate Images   │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Face Similarity    │
                         │     Matching       │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Social Verification│
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │  Evidence Object   │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │      SHA-256       │
                         │    Fingerprint     │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Ethereum Sepolia   │
                         │    Blockchain       │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Blockchain Readback │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Fingerprint Match  │
                         └─────────┬──────────┘
                                   │
                                   ▼
                              VERIFIED
```

---

## Project Structure

```text
Face-Identification-Blockchain-Verification/
│
├── input/
│   ├── .gitkeep
│   ├── test.jpg
│   └── test_same.jpg
│
├── models/
│   ├── face_detection_yunet_2023mar.onnx
│   └── face_recognition_sface_2021dec.onnx
│
├── results/
│   └── .gitkeep
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── evidence_hasher.py
│   │
│   ├── face/
│   │   ├── __init__.py
│   │   ├── detector.py
│   │   ├── encoder.py
│   │   └── comparator.py
│   │
│   ├── search/
│   │   ├── __init__.py
│   │   ├── visual_search.py
│   │   ├── image_downloader.py
│   │   ├── candidate_matcher.py
│   │   └── social_verifier.py
│   │
│   └── blockchain/
│       ├── __init__.py
│       ├── connection.py
│       ├── wallet.py
│       ├── balance.py
│       ├── recorder.py
│       ├── verifier.py
│       └── transaction.py
│
├── tests/
│   ├── test_setup.py
│   ├── test_models.py
│   ├── test_detector.py
│   ├── test_encoder.py
│   ├── test_comparator.py
│   ├── test_evidence_hasher.py
│   ├── test_serpapi.py
│   ├── test_visual_search.py
│   ├── test_image_downloader.py
│   ├── test_candidate_matcher.py
│   ├── test_social_matches.py
│   ├── test_social_verifier.py
│   ├── test_blockchain_connection.py
│   ├── test_wallet.py
│   ├── test_recorder.py
│   ├── test_verifier.py
│   └── ...
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Core Modules

| Module                 | Responsibility                             |
| ---------------------- | ------------------------------------------ |
| `detector.py`          | Detects faces using YuNet                  |
| `encoder.py`           | Generates face embeddings using SFace      |
| `comparator.py`        | Calculates face similarity                 |
| `visual_search.py`     | Performs visual search through SerpApi     |
| `image_downloader.py`  | Downloads candidate images                 |
| `candidate_matcher.py` | Processes and ranks candidate faces        |
| `social_verifier.py`   | Verifies social-media candidates           |
| `evidence_hasher.py`   | Generates SHA-256 fingerprints             |
| `connection.py`        | Connects to Ethereum Sepolia               |
| `wallet.py`            | Handles blockchain wallet operations       |
| `balance.py`           | Checks wallet balance                      |
| `recorder.py`          | Records fingerprints on the blockchain     |
| `verifier.py`          | Reads and verifies blockchain fingerprints |
| `transaction.py`       | Handles blockchain transaction operations  |
| `main.py`              | Runs the complete end-to-end pipeline      |

---

## Technology Stack

| Technology       | Purpose                             |
| ---------------- | ----------------------------------- |
| Python           | Core programming language           |
| OpenCV           | Computer vision and face processing |
| YuNet            | Face detection                      |
| SFace            | Face recognition and embeddings     |
| SerpApi          | Search API integration              |
| Google Lens      | Visual search                       |
| Web3.py          | Ethereum interaction                |
| Ethereum Sepolia | Blockchain test network             |
| NumPy            | Numerical operations                |
| Pillow           | Image processing                    |
| Requests         | HTTP requests                       |
| python-dotenv    | Environment variable management     |

---

## Example Output

A successful end-to-end execution produces output similar to:

```text
FACE IDENTIFICATION & VERIFICATION

Pipeline starting...

Input faces detected: 1
Input face encoded.

Visual candidates found: 59
Social candidates found: 20

Best social candidate:
----------------------------------------------------------------------
Platform: Facebook
Title: Albert Einstein's role in the Manhattan Project
Similarity: 0.9404

SHA-256 fingerprint:
3961d219dbb68f430721ce48354c8201b1cc2711d87d5b809f14c3d7e87f222f

Recording fingerprint on blockchain...

Blockchain record created:
----------------------------------------------------------------------
Transaction status: 1

Verifying fingerprint on blockchain...

Blockchain verification:
----------------------------------------------------------------------
Local fingerprint:
3961d219dbb68f430721ce48354c8201b1cc2711d87d5b809f14c3d7e87f222f

Blockchain fingerprint:
3961d219dbb68f430721ce48354c8201b1cc2711d87d5b809f14c3d7e87f222f

Verification result:
MATCH
VERIFIED
```

---

## Advantages

### End-to-End Automation

The complete process is handled through a single pipeline, from input image to blockchain verification.

### Face-Based Candidate Verification

Candidates are not selected solely from search results. Their detected faces are also compared against the input face.

### Multiple Evidence Sources

The pipeline combines visual search results and social-media information to identify potentially relevant evidence.

### Cryptographic Integrity

SHA-256 provides a fixed-length fingerprint that can be used to represent the generated evidence.

### Blockchain Verification

The fingerprint is recorded on Ethereum, allowing the stored value to be retrieved and independently compared with the local value.

### Modular Architecture

Face processing, search, evidence hashing, and blockchain functionality are separated into different modules, making the project easier to understand, test, and maintain.

---

## Limitations

This project is a **prototype and educational implementation**.

* Face similarity does not guarantee real-world identity.
* Visual search results depend on external services.
* Social-media content can change or become unavailable.
* Search APIs may have usage limits.
* The Sepolia network is a testnet.
* The system requires an internet connection for external services.
* Similarity scores should be treated as ranking evidence rather than absolute proof of identity.
* The blockchain stores the fingerprint rather than the original image or complete evidence.

---

## Installation

### 1. Clone the repository

```powershell
git clone <repository-url>
cd Face-Identification-Blockchain-Verification
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root using `.env.example` as a template.

```text
ENVIRONMENT=development

SERPAPI_KEY=your_serpapi_api_key_here
SEPOLIA_RPC_URL=your_sepolia_rpc_url_here
WALLET_PRIVATE_KEY=your_wallet_private_key_here
```

### Required credentials

| Variable             | Purpose                        |
| -------------------- | ------------------------------ |
| `SERPAPI_KEY`        | Access to SerpApi              |
| `SEPOLIA_RPC_URL`    | Connection to Ethereum Sepolia |
| `WALLET_PRIVATE_KEY` | Signs blockchain transactions  |

**Never commit `.env` or private keys to the repository.**

---

## Running the Project

Activate the virtual environment and run:

```powershell
python -m src.main
```

The complete pipeline will execute automatically.

A successful run should end with:

```text
MATCH
VERIFIED
```

---

## Testing

The project contains tests for the major components of the system, including:

```text
Setup
Models
Face Detection
Face Encoding
Face Comparison
Evidence Hashing
SerpApi
Visual Search
Image Downloading
Candidate Matching
Social Verification
Blockchain Connection
Wallet
Blockchain Recording
Blockchain Verification
```

Individual tests can be executed using Python module execution:

```powershell
python -m tests.test_setup
```

For the complete system:

```powershell
python -m src.main
```

---

## Security

Sensitive credentials are stored using environment variables.

The following should never be committed to GitHub:

```text
.env
API keys
Private keys
Wallet credentials
```

The `.env` file is excluded through `.gitignore`.

Only `.env.example`, containing placeholder values, should be included in the repository.

---

## Project Status

### Current Status: Core Pipeline Complete

| Component                | Status |
| ------------------------ | :----: |
| Project Setup            |    ✅   |
| Face Detection           |    ✅   |
| Face Encoding            |    ✅   |
| Face Similarity Matching |    ✅   |
| Visual Search            |    ✅   |
| Candidate Ranking        |    ✅   |
| Social Search            |    ✅   |
| Social Verification      |    ✅   |
| Evidence Generation      |    ✅   |
| SHA-256 Fingerprinting   |    ✅   |
| Ethereum Connection      |    ✅   |
| Blockchain Recording     |    ✅   |
| Blockchain Readback      |    ✅   |
| Fingerprint Verification |    ✅   |
| End-to-End Pipeline      |    ✅   |
| Git Repository Cleanup   |    ✅   |

### Final Verification

The complete pipeline has been successfully tested with a real Ethereum Sepolia transaction.

The local SHA-256 fingerprint was successfully compared against the fingerprint retrieved from the blockchain:

```text
Local Fingerprint
        =
Blockchain Fingerprint

        ↓

MATCH

        ↓

VERIFIED
```

---

## Future Improvements

Possible future improvements include:

* Better handling of images containing multiple faces
* Improved candidate filtering
* More advanced confidence and similarity scoring
* Additional search providers
* Additional social-media sources
* Web-based user interface
* Evidence history and storage
* Blockchain explorer integration
* Automated verification reports
* Improved API error handling
* Production-ready deployment

---

## License

This project is intended for educational and experimental purposes.

---

## Author

**Devendra Singh**

Computer Science & Engineering Student
