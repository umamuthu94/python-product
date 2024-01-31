# from flask import Flask, request, jsonify
# from models import Customer, CustomerInfo, Database
# from bson import ObjectId

# app = Flask(__name__)
# db = Database()

# @app.route('/customers', methods=['GET'])
# def get_customers():
#     customers = list(db.customers_collection.find())
#     customers = [
#         {"firstname": customer.get("firstname"), "lastname": customer.get("lastname")}
#         for customer in customers
#     ]
#     return jsonify(customers)


# @app.route('/customers', methods=['POST'])
# def create_customer():
#     data = request.get_json()
#     new_customer = Customer(**data)
#     customer_dict = new_customer.__dict__
#     result = db.customers_collection.insert_one(customer_dict)
#     return jsonify({"message": "Customer created successfully"})

# # Routes for CustomerInfo
# @app.route('/customerinfo', methods=['GET'])
# def get_customer_info():
#     customer_info_list = list(db.customer_info_collection.find())
#     customer_info_list = [
#         {
#             "firstname": customerinfo.get("firstname"),
#             "address": customerinfo.get("address"),
#             "mobileno": customerinfo.get("mobileno"),
#             "email": customerinfo.get("email")
#         }
#         for customerinfo in customer_info_list
#     ]
#     return jsonify(customer_info_list)

# @app.route('/customerinfo', methods=['POST'])
# def create_customer_info():
#     data = request.get_json()
#     new_customer_info = CustomerInfo(**data)
#     customer_info_dict = new_customer_info.__dict__
#     result = db.customer_info_collection.insert_one(customer_info_dict)
#     return jsonify({"message": "CustomerInfo created successfully"})



# if __name__ == '__main__':
#     app.run(debug=True)


from fastapi import FastAPI
from models import Customer, CustomerInfo
from database import Database

app = FastAPI()
db = Database()


@app.get('/customers')
async def get_customers():
    customers = list(db.customers_collection.find())
    customers = [
        {"firstname": customer.get("firstname"), "lastname": customer.get("lastname")}
        for customer in customers
    ]
    return customers

@app.post('/customers')
async def create_customer(customer: Customer):
    customer_dict = customer.dict()
    result = db.customers_collection.insert_one(customer_dict)
    return {"message": "Customer created successfully"}

@app.get('/customerinfo')
async def get_customer_info():
    customer_info_list = list(db.customer_info_collection.find())
    customer_info_list = [
        {
            "firstname": customerinfo.get("firstname"),
            "address": customerinfo.get("address"),
            "mobileno": customerinfo.get("mobileno"),
            "email": customerinfo.get("email")
        }
        for customerinfo in customer_info_list
    ]
    return customer_info_list

@app.post('/customerinfo')
async def create_customer_info(customer_info: CustomerInfo):
    customer_info_dict = customer_info.dict()
    result = db.customer_info_collection.insert_one(customer_info_dict)
    return {"message": "CustomerInfo created successfully"}
