from dataclasses import dataclass
from crypto import Crypto


@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: int
    signature: str


class Ledger:
    transactions = []

    def add(self, sender, receiver, amount, signature):
        transaction = Transaction(sender, receiver, amount, signature)
        self.transactions.append(transaction)

    def print(self, name):
        print(f"{name}'s Ledger")
        for transaction in self.transactions:
            print(
                f"{transaction.sender} > {transaction.amount} > {transaction.receiver} {transaction.signature[:10]}"
            )
