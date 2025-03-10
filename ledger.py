from dataclasses import dataclass
from crypto import Crypto
from transaction import Transaction


class Ledger:
    def __init__(self):
        self.transactions = []

    def add(self, transaction: Transaction):
        self.transactions.append(transaction)
        return transaction

    def create_transaction(self, sender, receiver, amount, signature, transaction_fee):
        return Transaction(
            sender_public_key=sender,
            receiver_public_key=receiver,
            amount=amount,
            signature=signature,
            transaction_fee=transaction_fee,
            input=[],
            output=[],
        )

    def print(self, name):
        print(f"{name}'s Ledger")
        for transaction in self.transactions:
            sender_short_key = "".join(transaction.sender_public_key.split("\n")[2:])[
                :5
            ]
            receiver_short_key = "".join(
                transaction.receiver_public_key.split("\n")[2:]
            )[:5]
            print(
                f"{sender_short_key} > {transaction.amount} > {receiver_short_key} {transaction.signature[:10]} {transaction.hash_value[:10]} {transaction.transaction_fee}"
            )
