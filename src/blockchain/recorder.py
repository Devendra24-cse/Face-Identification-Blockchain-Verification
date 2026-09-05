from src.blockchain.connection import BlockchainConnection
from src.blockchain.wallet import Wallet
from web3.exceptions import TimeExhausted


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

        try:
            receipt = (
                self.web3.eth.wait_for_transaction_receipt(
                    tx_hash,
                    timeout=120
                )
            )

        except TimeExhausted:

            print(
                "\nTransaction confirmation timed out."
            )

            print(
                "Checking transaction status..."
            )

            transaction = self.web3.eth.get_transaction(
                tx_hash
            )

            if transaction["blockNumber"] is None:

                raise RuntimeError(
                    "Transaction was submitted but "
                    "has not been mined yet."
                )

            receipt = (
                self.web3.eth.get_transaction_receipt(
                    tx_hash
                )
            )

        return {
            "transaction_hash": tx_hash.hex(),

            "block_number": receipt.blockNumber,

            "status": receipt.status,

            "gas_used": receipt.gasUsed,
        }