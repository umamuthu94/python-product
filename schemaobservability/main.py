from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


# MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Product_Info'
mongo = PyMongo(app)
collection = mongo.db.product_details


# @app.route('/product_details', methods=['GET'])
# def get_product_details():
#     results = []
#     for document in collection.find():
#         document['_id'] = str(document['_id'])
#         document_dict = {key: value for key, value in document.items() if key != '_id'}
#         results.append(document_dict)
#     return jsonify(results)

# @app.route('/product_details', methods=['POST'])
# def add_product_details():
#     data = request.get_json()
#     result = collection.insert_one(data)
#     return jsonify({'message': 'Product details added successfully'})


@app.route('/product_details', methods=['GET'])
def get_product_details():
    """
    Get product details
    ---
    responses:
      200:
        description: A list of product details
    """
    results = []
    for document in collection.find():
        document['_id'] = str(document['_id'])
        document_dict = {key: value for key, value in document.items() if key != '_id'}
        results.append(document_dict)
    return jsonify(results)


@app.route('/product_details', methods=['POST'])
def add_product_details():
    """
    Add product details
    ---
    parameters:
      - name: data
        in: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Product details added successfully
    """
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({'message': 'Product details added successfully'})



@app.route('/product_details/<firstname>', methods=['PUT'])
def update_product_details(firstname):
    """
    Update product details by firstname
    ---
    parameters:
      - name: firstname
        in: path
        type: string
        required: true
        description: The firstname of the product details to be updated
      - name: data
        in: body
        required: true
        schema:
          type: object
    responses:
      204:
        description: Product details updated successfully
      404:
        description: No product details found for the given firstname
    """
    data = request.get_json()
    result = collection.update_one({'firstname': firstname}, {'$set': data})
    if result.modified_count > 0:
        return '', 204  # 204 No Content
    else:
        return jsonify({'message': 'No product details found for the given firstname'}), 404



@app.route('/product_details/<firstname>', methods=['DELETE'])
def delete_product_details(firstname):
    """
    Delete product details by firstname
    ---
    parameters:
      - name: firstname
        in: path
        type: string
        required: true
        description: The firstname of the product details to be deleted
    responses:
      204:
        description: Product details deleted successfully
      404:
        description: No product details found for the given firstname
    """
    result = collection.delete_one({'firstname': firstname})
    if result.deleted_count > 0:
        return '', 204  # 204 No Content
    else:
        return jsonify({'message': 'No product details found for the given firstname'}), 404


@app.route('/product_details/<firstname>', methods=['GET'])
def get_product_details_by_firstname(firstname):
    """
    Get product details by firstname
    ---
    parameters:
      - name: firstname
        in: path
        type: string
        required: true
        description: The firstname of the product details to be retrieved
    responses:
      200:
        description: Product details for the given firstname
    """
    document = collection.find_one({'firstname': firstname})
    if document:
        document['_id'] = str(document['_id'])
        result = {key: value for key, value in document.items() if key != '_id'}
        return jsonify(result)
    else:
        return jsonify({'message': 'No product details found for the given firstname'}), 404


@app.route('/product_details/city/<city>', methods=['GET'])
def get_product_details_by_city(city):
    """
    Get product details by city
    ---
    parameters:
      - name: city
        in: path
        type: string
        required: true
        description: The city of the product details to be retrieved
    responses:
      200:
        description: A list of product details for the given city
    """
    results = []
    for document in collection.find({'address.city': city}):
        document['_id'] = str(document['_id'])
        document_dict = {key: value for key, value in document.items() if key != '_id'}
        results.append(document_dict)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
