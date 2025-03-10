from dataclasses import dataclass
from crypto import Crypto


@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: int
    signature: str
    public_key: str


class Ledger:
    def __init__(self):
        self.transactions = []

    def add(self, sender, receiver, amount, signature, public_key):
        transaction = Transaction(sender, receiver, amount, signature, public_key)
        self.transactions.append(transaction)
        return transaction

    def print(self, name):
        print(f"{name}'s Ledger")
        for transaction in self.transactions:
            print(
                f"{transaction.sender} > {transaction.amount} > {transaction.receiver} {transaction.signature[:10]}"
            )
