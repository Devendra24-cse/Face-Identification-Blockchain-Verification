from src.blockchain.connection import BlockchainConnection
from src.blockchain.wallet import Wallet


blockchain = BlockchainConnection()
wallet = Wallet()


address = wallet.get_address()

balance_wei = blockchain.web3.eth.get_balance(
    address
)

balance_eth = blockchain.web3.from_wei(
    balance_wei,
    "ether"
)


print("Wallet address:")
print(address)

print("\nSepolia balance:")
print(balance_eth, "ETH")