from peer import Peer, BadPeer
from internet import Internet
import random, time

SPEED = 0.99
id = 0


def transaction(peer: Peer, amount, address):
    global id
    id = id + 1
    peer.send(amount, address)


def log_balance(network):
    global id
    msg = f"{id} STATE: "
    for peer in network.peers.values():
        msg += peer.address + " : " + str(peer.balance) + "\t\t "
    print(msg)


def main():
    network = Internet()
    a = Peer(network, address="A", balance=100)
    b = Peer(network, address="B", balance=100)
    c = Peer(network, address="C", balance=100)
    d = BadPeer(network, address="D", balance=100)

    e = BadPeer(network, address="E", balance=100)

    f = BadPeer(network, address="F", balance=100)
    while True:
        var = random.random()
        time.sleep(1 - SPEED)
        if var < 0.05:
            sender = random.choice([a, b, c, d, e, f])
            amount = random.randint(1, 10)
            transaction(sender, amount, network.get_random_peer(sender))
            log_balance(network)
            print()


if __name__ == "__main__":
    main()
