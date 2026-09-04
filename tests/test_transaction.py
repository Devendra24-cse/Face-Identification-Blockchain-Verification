from blockchain.transaction import BlockchainTransaction


print("Creating blockchain transaction...")

transaction = BlockchainTransaction()

tx_hash = transaction.send_test_transaction()


print("\nTransaction sent successfully!")

print("\nTransaction hash:")
print(tx_hash)