# from pymongo import MongoClient

# class Customer:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
        

# class CustomerInfo:
#     def __init__(self, firstname, address, mobileno, email) :
#         self.firstname = firstname
#         self.address = address
#         self.mobileno = mobileno
#         self.email = email
        
# class Database:
#     def __init__(self, db_name='python-product'):
#         self.client = MongoClient()
#         self.db = self.client[db_name]
#         self.customers_collection = self.db['customers']
#         self.customer_info_collection = self.db['customer_info'] 
        
from pydantic import BaseModel

class Customer(BaseModel):
    firstname: str
    lastname: str

class CustomerInfo(BaseModel):
    firstname: str
    address: str
    mobileno: str
    email: str
