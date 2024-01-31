from pymongo import MongoClient

class Database:
    def __init__(self, db_name='python-product'):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.customers_collection = self.db['customers']
        self.customer_info_collection = self.db['customer_info']
