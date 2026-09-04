from src.blockchain.connection import BlockchainConnection
from src.blockchain.wallet import Wallet


class BlockchainRecorder:

    def __init__(self):
        self.blockchain = BlockchainConnection()
        self.wallet = Wallet()

        self.web3 = self.blockchain.web3

    def record_fingerprint(self, fingerprint):

        sender = self.wallet.get_address()

        nonce = self.web3.eth.get_transaction_count(
            sender
        )

        gas_price = self.web3.eth.gas_price

        transaction = {
            "from": sender,

            "to": sender,

            "value": 0,

            "nonce": nonce,

            "chainId": self.web3.eth.chain_id,

            "gasPrice": gas_price,

            "data": self.web3.to_bytes(
                text=fingerprint
            ),
        }

        estimated_gas = self.web3.eth.estimate_gas(
            transaction
        )

        transaction["gas"] = estimated_gas

        signed_transaction = (
            self.wallet.sign_transaction(
                transaction
            )
        )

        tx_hash = self.web3.eth.send_raw_transaction(
            signed_transaction.raw_transaction
        )

        receipt = (
            self.web3.eth.wait_for_transaction_receipt(
                tx_hash
            )
        )

        return {
            "transaction_hash": tx_hash.hex(),

            "block_number": receipt.blockNumber,

            "status": receipt.status,

            "gas_used": receipt.gasUsed,
        }