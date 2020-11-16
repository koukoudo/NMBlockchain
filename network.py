import blockchain
from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

blockchain = blockchain.Blockchain()

node_identifier = str(uuid4())


@app.route('/transactions/new')
def new_transaction():
    values = request.args

    # Check that required fields are in post response
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    block_index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {
        'message': f'Transaction will be added to block {block_index}'
    }

    return response, 201


@app.route('/chain')
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return response


@app.route('/nodes/new')
def new_node():
    values = request.args

    nodes = values['nodes']
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New node/s added',
        'total_nodes': len(blockchain.nodes)
    }

    return response, 201


@app.route('/nodes/resolve')
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return response


@app.route('/mine')
def mine():
    # Get next proof
    last_block = blockchain.chain[len(blockchain.chain) - 1]
    proof = blockchain.proof_of_work(last_block)

    # Reward for mining
    blockchain.new_transaction(
        sender='0',
        recipient=node_identifier,
        amount=1
    )

    # Add new block to chain
    previous_hash = last_block.calc_hash()
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New block forged',
        'index': block.index,
        'transactions': block.transactions,
        'proof': block.proof,
        'previous_hash': block.previous_hash
    }

    return response


if __name__ == '__main__':
    app.run()
