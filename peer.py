from __future__ import annotations
import time
from typing import TYPE_CHECKING
from ledger import Ledger, Transaction
from crypto import Crypto

if TYPE_CHECKING:
    from internet import Internet


class Peer:
    network: Internet | None = None
    balance = 0
    address = 0
    public_key = ""
    private_key = ""

    def __init__(
        self,
        network: Internet | None = None,
        balance: int = 0,
        address: str = "",
    ):
        self.balance = balance
        self.address = address
        (self.private_key, self.public_key) = Crypto.generate_key_pair()
        self.network = network
        network.add_peer(self)
        self.ledger = Ledger()
        print(self.public_key, self.private_key)
        print("Peer created: {}".format(self.address))

    def send(self, amount: int, address: str):
        if amount > self.balance:
            self.log("Insufficient balance")
            return
        receiver = self.network.get_peer(address)
        receiver_public_key = receiver.public_key
        if receiver is None:
            self.log("Peer not found")
            return
        receiver.receive(amount)
        signature = Crypto.get_signature(
            f"{self.public_key}&{amount}&{receiver_public_key}", self.private_key
        )
        transaction = self.ledger.create_transaction(
            self.public_key, receiver_public_key, amount, signature, 10
        )
        self.balance -= amount
        self.network.broadcast_transaction(transaction)
        self.ledger.print(self.address)

    def receive(self, amount: int):
        self.balance += amount

    def incoming_transaction(self, transaction: Transaction):
        # Verify the transaction
        message = f"{transaction.sender_public_key}&{transaction.amount}&{transaction.receiver_public_key}"
        if Crypto.verify_signature(
            message, transaction.sender_public_key, transaction.signature
        ):
            self.ledger.add(transaction)
        else:
            self.log("\033[91mInvalid transaction\033[0m")

    def log(self, message: str):
        print("{}: {}".format(self.address, message))

    def logbalance(self):
        self.log(f"Balance: {self.balance}")


class BadPeer(Peer):
    pass
    # def send(self, amount: int, address: str):
    #     # This mf tries to steal money from other peers by adding a fake transaction to the ledger
    #     signature = Crypto.get_signature(
    #         f"{self.address}&{amount}&{address}", self.private_key
    #     )
    #     transaction = self.ledger.create_transaction(
    #         address, self.address, amount, signature, self.public_key
    #     )
    #     self.ledger.print(self.address)
    #     self.network.broadcast_transaction(transaction)
