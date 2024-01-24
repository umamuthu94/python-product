from pymongo import MongoClient

class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
class Database:
    def __init__(self, db_name='python-product'):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.customers_collection = self.db['customers']