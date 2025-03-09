import time
class Peer:
    network = None
    balance = 0
    address = 0
    public_key = 0
    private_key = 0

    def __init__(
        self,
        network = None,
        balance: int = 0,
        address: str = "",
        public_key: str = "",
        private_key: str = "",
    ):
        self.balance = balance
        self.address = address
        self.public_key = public_key
        self.private_key = private_key
        self.network = network
        network.add_peer(self)
        print("Peer created: {}".format(self.address))


    def send(self, amount: int, address: str):
        if amount > self.balance:
            self.log("Insufficient balance")
            return
        self.log(f"Sending {amount} to {address}")
        time.sleep(.5)
        reciever = self.network.get_peer(address)
        if reciever is None:
            self.log("Peer not found")
            return
        reciever.receive(amount)
        self.balance -= amount
        self.logbalance()

    def receive(self, amount: int):
        self.balance += amount
        self.log(f"Received {amount}")
        self.logbalance()

    def log(self, message: str):
        print("{}: {}".format(self.address, message))
    def logbalance(self):
        self.log(f"Balance: {self.balance}")