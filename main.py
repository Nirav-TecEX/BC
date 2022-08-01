from datetime import datetime
import random

from blockchain.single_tx import SingleTransaction
from blockchain import block

def create_block(prev_hash, prev_id, timestamp):
    return block.Block(prev_hash, prev_id, timestamp)

def update_block(Blck: block.Block, transaction):
    response = Blck.add_transaction(transaction)
    if response == 1:
        print("Block added sucessfully")
    else:
        return response

def create_transactions(n=30):
    transactions = {}
    
    for i in range(0, 30):
        tx = SingleTransaction(i, "ABC", "abc", random.random(), str(datetime.now()))
        tx_hash = None

        transactions[i] = {"tx": tx, "hash": tx_hash}
    
    return transactions

def create_genesis_block():
    genesis_block = block.Block('genesis', 0, str(datetime.now()))
    genesis_block.hash_block()
    return genesis_block

if __name__ == "__main__":
    print("############## Creating Genesis Block ##############")
    my_chain = ['starting']
    my_chain.append(create_genesis_block())

    print("############## Creating Blocks ##############")
    prev_block_id = len(my_chain)-1
    prev_block = my_chain[prev_block_id]
    prev_hash = prev_block.get_block_hash()


    empty_block = create_block(prev_hash, prev_block_id, str(datetime.now()))


    print("############## Creating transactions ##############")
    transactions = create_transactions()

    current_block_id = len(my_chain)
    for i in transactions:
        # try adding to top block
        if empty_block.have_capacity():
            print(f"\t Transac: {i}\t Block: {current_block_id}")
            transactions[i]['tx'].set_my_block_id(current_block_id)
            transactions[i]["hash"] = transactions[i]['tx'].hash_transaction()
            empty_block.add_transaction(transactions[i])

            if not empty_block.have_capacity():
                empty_block.hash_block()
                my_chain.append(empty_block)

                prev_block_id = len(my_chain)-1
                prev_block = my_chain[prev_block_id]
                prev_hash = prev_block.get_block_hash()
                empty_block = create_block(prev_hash, prev_block_id, str(datetime.now()))

                current_block_id = len(my_chain)


    print("To access transactions use: \n\t my_chain[X].__dict__['_Block__transactions'][Y]['tx'].__dict__")

# print(tx_1.hash_transaction())
