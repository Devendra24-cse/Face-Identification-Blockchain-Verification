from src.blockchain.recorder import BlockchainRecorder


fingerprint = (
    "3961d219dbb68f430721ce48354c8201"
    "b1cc2711d87d5b809f14c3d7e87f222f"
)


print("Testing blockchain fingerprint recording...")
print()
print("Fingerprint:")
print(fingerprint)


recorder = BlockchainRecorder()


result = recorder.record_fingerprint(
    fingerprint
)


print("\nBlockchain record created!")
print("-" * 60)

print("Transaction hash:")
print(result["transaction_hash"])

print("\nBlock number:")
print(result["block_number"])

print("\nTransaction status:")
print(result["status"])
