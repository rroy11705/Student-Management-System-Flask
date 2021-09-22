from config import client, DATABASE
from flask import request, jsonify, make_response
from app import app
import secrets


@app.route("/api/create-user", methods=["POST"])
def add_user():

    try:
        req = request.get_json()
        name = req['name']
        email = req['email']
        collection = DATABASE['students']

        if not collection.find_one({"email": email}):
            user_id = secrets.token_hex(16)
            record = {
                '_id': user_id,
                'name': name,
                'email': email,
                'state': req['state'],
                'city': req['city'],
                'address': req['address'],
                'phone': req['phone']
            }
            collection.insert_one(record)
            res = {
                'user_id': user_id
            }
            return make_response(jsonify(res), 201)
        else:
            res = {
                'message': 'email id already exist'
            }
            return make_response(jsonify(res), 200)

    except:
        res = {
            'message': 'some error occurred, try later'
        }
        return make_response(jsonify(res), 503)


@app.route("/api/get-user/<user_id>")
def get_user(user_id):

    try:
        collection = DATABASE['students']
        user = collection.find_one({'_id': user_id}, {'_id': 0})
        res = {
            'data': user
        }
        return make_response(jsonify(res), 200)

    except:
        res = {
            'message': 'some error occurred, try later'
        }
        return make_response(jsonify(res), 503)


@app.route("/api/update-user/<user_id>", methods=['PUT'])
def update_user(user_id):

    try:
        collection = DATABASE['students']
        if collection.find_one({"_id": user_id}):
            req = request.get_json()
            new_values = {"$set": req}
            collection.update_one({'_id': user_id}, new_values)
            res = {
                'status': 'success',
                'message': 'updated successfully'
            }
            return jsonify(res)
        else:
            res = {
                'status': 'failure',
                'message': 'user not found'
            }
            return jsonify(res)

    except:
        res = {
            'message': 'some error occurred, try later'
        }
        return make_response(jsonify(res), 503)


@app.route("/api/delete-user/<user_id>", methods=["DELETE"])
def delete_user(user_id):

    try:
        collection = DATABASE['students']
        collection.delete_one({'_id': user_id})
        res = {
            'message': 'user updated successfully'
        }
        return make_response(jsonify(res), 204)

    except:
        res = {
            'message': 'some error occurred, try later'
        }
        return make_response(jsonify(res), 503)
