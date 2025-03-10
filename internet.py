from peer import Peer
import random
from ledger import Transaction


class Internet:
    peer_count = 0
    peers = {}

    def __init__(self):
        print("Initialised Internet")

    def get_peer(self, address: str) -> Peer | None:
        if address in self.peers:
            return self.peers[address]
        else:
            return None

    def get_peers(self):
        return self.peers

    def add_peer(self, peer: Peer):
        self.peers[peer.address] = peer
        self.peer_count += 1

    def get_random_peer(self, peer):
        available_peers = self.peers.copy()
        if peer.address in self.peers:
            del available_peers[peer.address]
        return random.choice(list(available_peers.keys()))

    def broadcast_transaction(self, transaction: Transaction):
        for peer in self.peers.values():
            if transaction.sender != peer.address:
                peer.incoming_transaction(transaction)

    def log_data(self):
        print("Peer count: ", self.peer_count)

    def log_balance(self):
        msg = "STATE: "
        for peer in self.peers.values():
            msg += peer.address + " : " + str(peer.balance) + "\t\t "
        print(msg)
