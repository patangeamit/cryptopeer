from peer import Peer
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
    
    def add_peer(self, peer: Peer):
        self.peers[peer.address] = peer
        self.peer_count += 1

    def log_data(self):
        print("Peer count: ", self.peer_count)