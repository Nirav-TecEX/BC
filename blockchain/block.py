from hashlib import sha512
import json
import time

class Block:
    
    block_length = 3

    def __init__(self, prev_hash, prev_id, timestamp):
        """ Block constructor. 
            A block is created whenever there are a certain number 
            of transactions. 
            :param self.transactions   ::  list
            :param self.prev_hash      ::  str
            :param self.timestamp      ::  datetime to str
            :param self.nonce          ::  int """

        self.header = {"prev_block_hash":prev_hash,
                       "prev_block_id":prev_id,
                       "created_timestamp":timestamp}
        self.__transactions = []
        self.nonce = 0

    def add_transaction(self, transaction):
        if len(self.__transactions) < self.block_length:
            self.__transactions.append(transaction)
            return 1
        else:
            return transaction

    @property
    def __block_hasher__(self):
        """ Returns hash of block after convertnig
            to JSON string """
        # transaction_json_string = json.dumps(self.__dict__, sort_keys=True)
        transaction_json_string = self.toJSON()
        return sha512(transaction_json_string.encode()).hexdigest()
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def hash_block(self):
        return self.__block_hasher__ 

    def get_block_hash(self):
        if hasattr(self, '__block_hasher__'):
            return self.__block_hasher__  
    
    def have_capacity(self):
        if len(self.__transactions) < self.block_length:
            return True
        else:
            return False
