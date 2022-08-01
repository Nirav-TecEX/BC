# from block import Block
import block

def create_block(prev_hash, prev_id, timestamp):
    return block.Block(prev_hash, prev_id, timestamp)

def update_block(Blck: block.Block, transaction):
    response = Blck.add_transaction(transaction)
    if response == 1:
        print("Block added sucessfully")
    else:
        return response