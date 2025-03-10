import time
from ledger import Ledger, Transaction
from crypto import Crypto


class Peer:
    network = None
    balance = 0
    address = 0
    public_key = ""
    private_key = ""

    def __init__(
        self,
        network=None,
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
        reciever = self.network.get_peer(address)
        if reciever is None:
            self.log("Peer not found")
            return
        reciever.receive(amount)
        signature = Crypto.get_signature(
            f"{self.address}&{amount}&{address}", self.private_key
        )
        transaction = self.ledger.add(self.address, address, amount, signature, self.public_key)
        self.ledger.print(self.address)
        self.balance -= amount
        self.network.broadcast_transaction(transaction)

    def receive(self, amount: int):
        self.balance += amount

    def incoming_transaction(self, transaction: Transaction):
        # Verify the transaction
        message = f"{transaction.sender}&{transaction.amount}&{transaction.receiver}"
        if Crypto.verify_signature(message, transaction.public_key, transaction.signature):
            self.ledger.add(transaction.sender, transaction.receiver, transaction.amount, transaction.signature, transaction.public_key)
        else:
            self.log("Invalid transaction")

    def log(self, message: str):
        print("{}: {}".format(self.address, message))

    def logbalance(self):
        self.log(f"Balance: {self.balance}")
