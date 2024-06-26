from backend.blockchain.block import Block
class Blockchain:
    """
    Blockchain:a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain=[Block.genesis()]

    def add_block(self,data):
        self.chain.append(Block.mine_block(self.chain[-1],data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

block1=Blockchain()
block1.add_block('one')
block1.add_block('two')
print(block1)
