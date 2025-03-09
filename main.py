from peer import Peer
from internet import Internet
import random, time
SPEED = .05
def main():
    network = Internet()
    a = Peer(network, address="A", balance=100)
    b = Peer(network, address="B")
    while True:
        var = random.random()
        time.sleep(SPEED)
        if var < 0.05:
            a.send(10, "B")
            print()
if __name__ == "__main__":
    main()
