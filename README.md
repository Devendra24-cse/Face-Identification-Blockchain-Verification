# Face Identification & Blockchain Verification

A Python-based pipeline that combines face analysis, visual web search, social-media verification, evidence hashing, and blockchain-based fingerprint verification.

## Overview

The system takes an input face image and processes it through multiple stages:

Input Image
→ Face Detection
→ Face Encoding
→ Visual Web Search
→ Candidate Image Matching
→ Social-Media Verification
→ Evidence Generation
→ SHA-256 Fingerprint
→ Ethereum Sepolia
→ Blockchain Verification

The purpose of the blockchain component is to record a cryptographic fingerprint of the generated evidence and verify that the same fingerprint can be retrieved from the blockchain later.

## Features

- Face detection using YuNet
- Face encoding using SFace
- Face similarity comparison
- Google Lens visual search through SerpApi
- Candidate image downloading
- Candidate face matching and ranking
- Social-media candidate verification
- Evidence object generation
- SHA-256 evidence fingerprinting
- Ethereum Sepolia testnet recording
- Blockchain fingerprint readback
- Local vs blockchain fingerprint verification

## Project Structure

```text
Face-Identification-Blockchain-Verification/
│
├── input/
│   ├── test.jpg
│   └── test_same.jpg
│
├── models/
│   ├── sface/
│   │   └── face_recognition_sface_2021dec.onnx
│   └── yunet/
│       └── face_detection_yunet_2026may.onnx
│
├── results/
│
├── src/
│   ├── blockchain/
│   ├── face/
│   ├── search/
│   ├── evidence_hasher.py
│   └── main.py
│
├── tests/
│   └── test_*.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
