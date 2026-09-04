from blockchain.connection import BlockchainConnection


print("Connecting to Sepolia...")


blockchain = BlockchainConnection()


if blockchain.is_connected():

    print("Connection successful!")

    print(
        "Chain ID:",
        blockchain.get_chain_id()
    )

    print(
        "Latest block:",
        blockchain.get_latest_block()
    )

else:

    print("Connection failed.")