from flask import Flask, request, jsonify
from models import Customer, Database

app = Flask(__name__)
db = Database()

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = list(db.customers_collection.find())
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = Customer(**data)
    db.customers_collection.insert_one(new_customer.__dict__)
    return jsonify({"message": "Customer created successfully"})

if __name__ == '__main__':
    app.run(debug=True)
