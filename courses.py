# from flask import Flask, request, make_response
# from flask_restful import Resource, Api
from pymongo import MongoClient
import json

# Basic Setup
# 1
# app = Flask(__name__)
# 2
# mongo = MongoClient('localhost', 27017)
# 3
# app.db = mongo.local
# 4
# api = Api(app)


# @app.route('/courses', methods=["GET", "POST"])
# def courses():
#     # courseDictionary = {"name": "Mathematics",
#     #                     "course_id": 7483,
#     #                     "students": ["Matthew", "Raymond", "Elmer"]}
#     # json_dictionary = json.dumps(courseDictionary)
#     # course_route_database = mongo.local.courses
#     # post_insertion = course_route_database.insert_one(json_dictionary).inserted_id
#     # post_insertion


if __name__ == '__main__':
    # app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    # app.run(debug=True)
    courseDictionary = {"name": "Mathematics",
                        "course_id": 7483,
                        "students": ["Matthew", "Raymond", "Elmer"]}
    # connect to mongo
    client = MongoClient('mongodb://localhost:27017/')
    # define our database
    db = client['courses']
    #creating collection
    records = db.records #create collection
    #drop database
    records.drop()
    print ("the database is: ")
    #inserts one document
    records.insert_one(courseDictionary)
    records.insert_one({"name": "Biology",
                        "course_id": 4567,
                        "students": ["Corey", "Raymond", "Elmer"]})

    found = records.find({}) #finds all records
    print (found)
    for record in found:
        print (record)
