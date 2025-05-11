# 🌐 Distributed Key-Value Store with Consensus Algorithms

A Python implementation of a fault-tolerant distributed system simulating Paxos and Raft consensus protocols.

## 📌 Features

- **Two consensus algorithms**:
  - 🧩 **Paxos** for basic distributed agreement
  - 🚢 **Raft** for leader election and log replication
- **Network simulation**:
  - 📨 Message passing between nodes
  - 💥 Node failure simulation
- **Key-value store**:
  - 🔑 Simple in-memory storage
  - 🔄 Replication via consensus

## 🛠️ Setup

# Clone repository
git clone https://github.com/ArasEmin/Distributed-Key-Value-Store.git
cd Distributed-Key-Value-Store

# Install dependencies (none required for basic simulation)
python -m pip install -r requirements.txt  # Optional for visualization
🚀 Running the Simulation
Basic Paxos Demo
bash
python main.py --algorithm paxos
Output:

Node 1 → Node 2: PROPOSE (proposal_id=1)
Node 1 → Node 3: PROPOSE (proposal_id=1)
Node 2 received PROMISE for proposal 1
Raft Leader Election
bash
python main.py --algorithm raft
Output:

Node 1 started election (term=1)
Node 2 → Node 1: VOTE_GRANTED
Node 1 became LEADER for term 1
📂 Project Structure
.
├── consensus/           # Consensus algorithms
│   ├── paxos.py         # Paxos implementation
│   └── raft.py          # Raft implementation
├── tests/               # Unit tests
├── node.py              # Node network behavior
├── message.py           # Message protocol
└── main.py              # Simulation entry point
🧪 Testing
bash
# Run all tests
pytest tests/

# Test specific algorithm
pytest tests/test_raft.py -v
🌟 Next Steps
Add persistent storage

Implement real network sockets

Build visualization dashboard

📜 License
MIT © ARAS EMIN
