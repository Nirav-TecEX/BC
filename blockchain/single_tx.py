from hashlib import sha512
import json

class SingleTransaction:
    def __init__(self, post_id, doctors_name, patients_name, additional_information, transaction_time):
        """ Single transaction hasher. 'Data' from TABLE single_transaction and stroes hash in it. 
            :param post_id: unique 'post_id'
            :param giver_of_loan: 'username'
            :param reciever_of_loan: 'other_username' 
            :param loan_amount: 'loan_amount'
            :param transaction_time: 'pay_time' """

        self.__post_id = post_id
        self.__doctors_name = doctors_name
        self.__patients_name = patients_name
        self.__additional_information = additional_information
        self.__transaction_time = transaction_time
        self.__my_block_id = None


    @property 
    def my_block_id(self):
        return self.__my_block_id

    def set_my_block_id(self, block_id):
        if self.__my_block_id is None:
            self.__my_block_id = block_id

    @property
    def __single_transaction_hasher__(self):
        """ Returns hash of block after convertnig
            to JSON string """

        transaction_json_string = json.dumps(self.__dict__, sort_keys=True)
        return sha512(transaction_json_string.encode()).hexdigest()
    
    def hash_transaction(self):
        return self.__single_transaction_hasher__
    