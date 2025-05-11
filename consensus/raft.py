from enum import Enum
import random
from message import Message, MessageType


class RaftState(Enum):
    FOLLOWER = 1
    CANDIDATE = 2
    LEADER = 3


class RaftNode:
    def __init__(self, node: 'Node'):
        self.node = node
        self.state = RaftState.FOLLOWER
        self.current_term = 0
        self.voted_for = None
        self.election_timeout = random.randint(150, 300)  # ms cinsinden

    def start_election(self):
        """Leader seçimini başlat"""
        self.state = RaftState.CANDIDATE
        self.current_term += 1
        self.voted_for = self.node.id

        # Diğer node'lara RequestVote mesajı gönder
        for peer in self.node.peers:
            msg = Message(
                sender_id=self.node.id,
                receiver_id=peer,
                type=MessageType.REQUEST_VOTE,
                data={
                    "term": self.current_term,
                    "candidate_id": self.node.id
                }
            )
            self.node.send(msg)

    def handle_vote_response(self, msg: Message):
        """Oyları işle ve lider olup olmadığını kontrol et"""
        if msg.data["term"] == self.current_term and self.state == RaftState.CANDIDATE:
            if self.count_votes() > len(self.node.peers) // 2:
                self.become_leader()

    def become_leader(self):
        """Lider olduğunda log replikasyonunu başlat"""
        self.state = RaftState.LEADER
        print(f"Node {self.node.id} is now LEADER for term {self.current_term}")
        # Heartbeat mesajları gönder
        self.send_heartbeats()

    def send_heartbeats(self):
        """Tüm follower'lara heartbeat gönder"""
        for peer in self.node.peers:
            msg = Message(
                sender_id=self.node.id,
                receiver_id=peer,
                type=MessageType.APPEND_ENTRIES,
                data={"term": self.current_term}
            )
            self.node.send(msg)
