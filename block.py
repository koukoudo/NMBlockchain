class Block:

    def __init__(self, index, timestamp, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof