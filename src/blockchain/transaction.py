from blockchain.connection import BlockchainConnection
from blockchain.wallet import Wallet


class BlockchainTransaction:

    def __init__(self):
        self.blockchain = BlockchainConnection()
        self.wallet = Wallet()

    def send_test_transaction(self):

        web3 = self.blockchain.web3
        account = self.wallet.account

        address = account.address

        nonce = web3.eth.get_transaction_count(
            address
        )

        gas_price = web3.eth.gas_price

        transaction = {
            "nonce": nonce,
            "to": address,
            "value": 0,
            "gas": 100000,
            "gasPrice": gas_price,
            "chainId": web3.eth.chain_id,
            "data": web3.to_hex(
                text="Blockchain test"
            ),
        }

        signed_transaction = account.sign_transaction(
            transaction
        )

        transaction_hash = web3.eth.send_raw_transaction(
            signed_transaction.raw_transaction
        )

        return transaction_hash.hex()