from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from message import Message, MessageType
    from node import Node


class PaxosNode:
    def __init__(self, node: 'Node'):
        self.node = node
        self.proposal_id = 0

    def prepare(self, key: str, value: str):
        """Paxos Phase 1: Prepare mesajlarını gönder"""
        from message import Message, MessageType  # Runtime'da kullanmak için

        self.proposal_id += 1
        for peer in self.node.peers:
            msg = Message(
                sender_id=self.node.id,
                receiver_id=peer,
                type=MessageType.PROPOSE,
                data={"key": key, "value": value, "proposal_id": self.proposal_id}
            )
            self.node.send(msg)

    def handle_promise(self, msg: 'Message'):
        """Paxos Phase 2: Promise'leri işle"""
        if msg.data["proposal_id"] == self.proposal_id:
            print(f"Node {self.node.id} received PROMISE for proposal {self.proposal_id}")
            # Accept mesajlarını gönder...