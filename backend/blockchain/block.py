import time
from backend.util.crypto_hash import crypto_hash
from backend.config import MINE_RATE

GENESIS_DATA={
    'timestamp':1,
    'last_hash':'genesis_last_hash',
    'hash':'genesis_hash',
    'data':[],
    'difficulty' : 3,
    'nonce':'genesis_nonce'
}

class Block:
    """
    Block:a unit of storage
    Store transaction in a blockchain that supports a 
    cryptocurrency
    """
    def __init__(self,timestamp,last_hash,hash,data,difficulty,nonce):
        self.timestamp=timestamp
        self.last_hash=last_hash
        self.hash=hash
        self.data=data
        self.difficulty=difficulty
        self.nonce=nonce
    
    def __repr__(self):
        return (
            f'data:{self.data}''\n'
            f'timestamp: {self.timestamp}''\n'
            f'last_hash:{self.last_hash}''\n'
            f'hash:{self.hash}''\n'
            f'difficulty:{self.difficulty}' '\n'
            f'nonce:{self.nonce}'
            '\n'
        )
    @staticmethod
    def mine_block(last_block,data):
        """
        Mine a block based on the given last_block and data,
        until is found that meets the leading 0's proof of work
        requirement.
        """
        timestamp=time.time_ns()
        last_hash=last_block.hash
        difficulty= Block.adjust_difficulty(last_block,timestamp)
        nonce = 0
        hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)
        
        while hash[0:difficulty]!='0'*difficulty:
            nonce += 1
            timestamp = time.time_ns()
            hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)

        return Block(timestamp,last_hash,hash,data,difficulty,nonce)
    
    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        # return Block(
        #     GENESIS_DATA['timestamp'],
        #     GENESIS_DATA['last_hash'], 
        #     GENESIS_DATA['hash'],
        #     GENESIS_DATA['data'])
        return Block(**GENESIS_DATA)
    @staticmethod
    def adjust_difficulty(last_block,new_timestamp):
        """
        Calculate the adjust difficulty according to the MINE_RATE
        Increase the difficulty for quickly mined blocks
        Decrease the difficulty for slowly mined blocks
        """ 
        if (new_timestamp - last_block.timestamp)<MINE_RATE:
            return last_block.difficulty + 1

        if(last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1

if __name__=='__main__':
    genesis_block=Block.genesis()
    block =Block.mine_block(genesis_block,'alvi')
    print(block)
