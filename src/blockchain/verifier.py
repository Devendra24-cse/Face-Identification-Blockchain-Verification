from src.blockchain.connection import BlockchainConnection


class BlockchainVerifier:

    def __init__(self):
        self.blockchain = BlockchainConnection()
        self.web3 = self.blockchain.web3

    def get_transaction_fingerprint(self, transaction_hash):

        transaction = self.web3.eth.get_transaction(
            transaction_hash
        )

        transaction_data = transaction["input"]

        fingerprint = transaction_data.decode(
            "utf-8"
        )

        return fingerprint

    def verify_fingerprint(
        self,
        local_fingerprint,
        transaction_hash
    ):

        blockchain_fingerprint = (
            self.get_transaction_fingerprint(
                transaction_hash
            )
        )

        is_match = (
            local_fingerprint
            == blockchain_fingerprint
        )

        return {
            "local_fingerprint": local_fingerprint,

            "blockchain_fingerprint":
                blockchain_fingerprint,

            "match": is_match
        }