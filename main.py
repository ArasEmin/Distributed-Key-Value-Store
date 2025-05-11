from node import Node
from consensus.paxos import PaxosNode

# 3 node'luk bir ağ oluştur
nodes = {
    1: Node(1, peers=[2, 3]),
    2: Node(2, peers=[1, 3]),
    3: Node(3, peers=[1, 2])
}

# Node 1 için Paxos başlat
paxos_node = PaxosNode(nodes[1])
paxos_node.prepare("name", "Alice")

# Node 2'yi fail yap (hata tolerans testi)
nodes[2].fail()
