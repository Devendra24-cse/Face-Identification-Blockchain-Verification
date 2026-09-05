from src.blockchain.wallet import Wallet


print("Loading wallet...")

wallet = Wallet()

print("Wallet loaded successfully!")

print(
    "Wallet address:",
    wallet.get_address()
)
