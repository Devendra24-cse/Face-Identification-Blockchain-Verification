from src.blockchain.connection import BlockchainConnection
from src.blockchain.wallet import Wallet


blockchain = BlockchainConnection()
wallet = Wallet()

web3 = blockchain.web3

sender = wallet.get_address()

balance = web3.eth.get_balance(sender)

print("Sender:")
print(sender)

print("\nBalance:")
print(web3.from_wei(balance, "ether"), "ETH")


# Send a very small amount of Sepolia ETH
amount = web3.to_wei(0.000001, "ether")

nonce = web3.eth.get_transaction_count(sender)

transaction = {
    "from": sender,
    "to": sender,
    "value": amount,
    "nonce": nonce,
    "chainId": web3.eth.chain_id,
    "gas": 21000,
    "gasPrice": web3.eth.gas_price,
}


signed_transaction = wallet.sign_transaction(transaction)

tx_hash = web3.eth.send_raw_transaction(
    signed_transaction.raw_transaction
)

print("\nTransaction submitted!")

print("Transaction hash:")
print(tx_hash.hex())


print("\nWaiting for confirmation...")

receipt = web3.eth.wait_for_transaction_receipt(
    tx_hash
)

print("\nTransaction confirmed!")

print("Block number:")
print(receipt.blockNumber)

print("Status:")
print(receipt.status)