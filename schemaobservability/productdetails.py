from pymongo import MongoClient

class Address:
    def __init__(self, address1, address2, city, state, pincode):
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.pincode = pincode

class Product:
    def __init__(self, name, description, price, categories):
        self.name = name
        self.description = description
        self.price = price
        self.categories = categories

class ProductDetails:
    def __init__(self, firstname, lastname, address, products):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.products = products

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['Product_Info']
collection = db['product_details']

# class Database:
#     def __init__(self, db_name= 'Product_Info'):
#         self.client = MongoClient()
#         self.db = self.client[db_name]
#         self.customers_collection = self.db['product_details']
