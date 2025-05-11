import random
from typing import Dict, List
from message import Message, MessageType

class Node:
    def __init__(self, node_id: int, peers: List[int]):
        self.id = node_id
        self.peers = peers  # Bağlı olduğu diğer node'ların ID'leri
        self.storage: Dict[str, str] = {}  # Key-value store
        self.failed = False  # Hata simülasyonu için

    def send(self, msg: Message):
        if self.failed:
            print(f"Node {self.id} is DOWN, cannot send messages!")
            return
        # Gerçekte bu mesaj bir ağ katmanına gider (burada simüle ediyoruz)
        print(f"Node {self.id} → Node {msg.receiver_id}: {msg.type.name}")

    def receive(self, msg: Message):
        if self.failed:
            print(f"Node {self.id} is DOWN, cannot receive messages!")
            return
        self.process_message(msg)

    def process_message(self, msg: Message):
        # Paxos veya Raft mantığı burada işletilir
        pass

    def fail(self):
        """Node'u hatalı duruma getir (simülasyon için)"""
        self.failed = True
