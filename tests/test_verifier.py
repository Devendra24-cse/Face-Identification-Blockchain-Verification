from src.blockchain.verifier import BlockchainVerifier


transaction_hash = (
    "5717b9c59554f535ad66769303383348279aaa0e96e932a3acac29f8b6e5b536"
)

local_fingerprint = (
    "3961d219dbb68f430721ce48354c8201"
    "b1cc2711d87d5b809f14c3d7e87f222f"
)


print("Verifying fingerprint...")
print()


verifier = BlockchainVerifier()


result = verifier.verify_fingerprint(
    local_fingerprint,
    transaction_hash
)


print("Local fingerprint:")
print(result["local_fingerprint"])

print("\nBlockchain fingerprint:")
print(result["blockchain_fingerprint"])

print("\nVerification result:")

if result["match"]:
    print("MATCH")
    print("VERIFIED")
else:
    print("MISMATCH")
    print("NOT VERIFIED")