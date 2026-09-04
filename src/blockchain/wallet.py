import os

from dotenv import load_dotenv
from eth_account import Account


class Wallet:

    def __init__(self):
        load_dotenv()

        private_key = os.getenv(
            "WALLET_PRIVATE_KEY"
        )

        if not private_key:
            raise ValueError(
                "WALLET_PRIVATE_KEY not found in .env"
            )

        self.account = Account.from_key(
            private_key
        )

    def get_address(self):
        return self.account.address

    def sign_transaction(self, transaction):
        return self.account.sign_transaction(transaction)