import os

from dotenv import load_dotenv
from web3 import Web3


class BlockchainConnection:

    def __init__(self):
        load_dotenv()

        rpc_url = os.getenv(
            "SEPOLIA_RPC_URL"
        )

        if not rpc_url:
            raise ValueError(
                "SEPOLIA_RPC_URL not found in .env"
            )

        self.web3 = Web3(
            Web3.HTTPProvider(rpc_url)
        )

    def is_connected(self):
        return self.web3.is_connected()

    def get_chain_id(self):
        return self.web3.eth.chain_id

    def get_latest_block(self):
        return self.web3.eth.block_number