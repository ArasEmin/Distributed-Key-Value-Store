from dataclasses import dataclass
from enum import Enum

class MessageType(Enum):
    PROPOSE = 1      # Değer önerme
    PROMISE = 2      # Paxos: Promise mesajı
    ACCEPT = 3       # Paxos: Accept mesajı
    ACCEPTED = 4     # Paxos: Accepted mesajı

@dataclass
class Message:
    sender_id: int
    receiver_id: int
    type: MessageType
    data: dict  # { "key": "value", "proposal_id": 123 }
