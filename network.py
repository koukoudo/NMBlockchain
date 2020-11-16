import blockchain
from flask import Flask

app = Flask(__name__)

blockchain = blockchain.Blockchain()


@app.route('/mine')
def mine():
    response = {
        'message': 'New block mined'
    }

    return response


@app.route('/transactions/new')
def new_transaction():
    response = {
        'message': 'Transaction will be added to thee next block'
    }

    return response


@app.route('/chain')
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return response


@app.route('/nodes/new')
def new_node():
    response = {
        'message': 'Node added',
        'total_nodes': len(blockchain.nodes)
    }

    return response


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


if __name__ == '__main__':
    app.run()
