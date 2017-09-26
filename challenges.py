from flask import Flask, request, make_response
from flask_restful import Resource, Api
from pymongo import MongoClient
import json

# Basic Setup
# 1
app = Flask(__name__)
# 2
mongo = MongoClient('localhost', 27017)
# 3
app.db = mongo.develop_database
# 4
api = Api(app)

# Method to post resources and then the method to retrieve them will be after
@app.route('/pets', methods=["POST", "GET"])
def pets_post():
    json_pets = {"pet_species": ["Cat", "Dog", "Snake", "Hamster", "Tiger"], "pet_name": ["Katy", "Spotty", "Sparrow"]}
    json_casting = json.dumps(json_pets)
    return (json_casting, 200, None)


# @app.route('/pets', methods=["GET"])
# def pets_get():





if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
