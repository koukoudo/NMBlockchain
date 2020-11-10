class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.nodes = set()

        self.new_block(proof=100, previous_hash='1')

    def new_block(self, proof, previous_hash):

    def new_transaction(self, sender, recipient, amount):

    def hash_block(self, block):

    def get_last_block(self, block):

    def register_node(self, address):

    def validate_chain(self, chain):

    def resolve_conflicts(self):

    def mine(self):