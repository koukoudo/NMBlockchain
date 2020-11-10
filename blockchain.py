import time
import hashlib
import json

class Block:
    def __init__(self, index, timestamp, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def calc_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        raw_hash = sha256(block_string.encode())
        hex_hash = raw_hash.hexdigest()
        return hex_hash

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.nodes = set()

        #Genesis block
        self.new_block(proof=100, previous_hash='1')

    def new_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, time(), self.current_transactions, proof, previous_hash)
        self.transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.transactions.append(transaction)
        return len(self.chain) - 1

    def register_node(self, address):

    def validate_chain(self, chain):

    def resolve_conflicts(self):

    def mine(self):