from evidence_hasher import EvidenceHasher


hasher = EvidenceHasher()


evidence = {
    "source": "Facebook",
    "title": "The last known photograph of Albert Einstein",
    "link": "https://www.facebook.com/example-post",
    "profile_name": None,
}


# Create first fingerprint
fingerprint_1 = hasher.create_fingerprint(
    evidence
)


# Create second fingerprint
fingerprint_2 = hasher.create_fingerprint(
    evidence
)


print("Fingerprint 1:")
print(fingerprint_1)

print("\nFingerprint 2:")
print(fingerprint_2)


print("\nHashes identical:")

if fingerprint_1 == fingerprint_2:
    print("YES")
else:
    print("NO")


print("\nHash length:")
print(len(fingerprint_1))