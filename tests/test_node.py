import pytest
from node import Node
from message import Message, MessageType


def test_node_initialization():
    node = Node(1, peers=[2, 3])
    assert node.id == 1
    assert not node.failed


def test_message_passing():
    node1 = Node(1, peers=[2])
    node2 = Node(2, peers=[1])

    msg = Message(
        sender_id=1,
        receiver_id=2,
        type=MessageType.PROPOSE,
        data={"key": "test"}
    )

    node1.send(msg)  # Console çıktısını kontrol etmek için
    node2.receive(msg)  # Hata olmamalı
