import time
from backend.util.crypto_hash import crypto_hash
class Block:
    """
    Block:a unit of storage
    Store transaction in a blockchain that supports a 
    cryptocurrency
    """
    def __init__(self,timestamp,last_hash,hash,data):
        self.timestamp=timestamp
        self.last_hash=last_hash
        self.hash=hash
        self.data=data
    
    def __repr__(self):
        return (
            f'data:{self.data}''\n'
            f'timestamp: {self.timestamp}''\n'
            f'last_hash:{self.last_hash}''\n'
            f'hash:{self.hash}''\n'
            '\n'
        )
    @staticmethod
    def mine_block(last_block,data):
        """
        Mine a block based on the given last_block and data
        """
        timestamp=time.time_ns()
        last_hash=last_block.hash
        hash=crypto_hash(timestamp,last_hash,data)
        return Block(timestamp,last_hash,hash,data)
    
    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        return Block(1,'genesis_last_hash', 'genesis_hash',[])


if __name__=='__main__':
    genesis_block=Block.genesis()
    block =Block.mine_block(genesis_block,'alvi')
    print(block)
