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
app.db = mongo.local
# 4
api = Api(app)


@app.route('/my_page', methods=["GET", "POST"])
def person_route():
    # json_person = {"name": ["Matthew", "Corey", "Latchman", "Micheal", "Superman", "Batman"], 'age': [33, 45, 22, 23, 23, 64, 64]}
    # json_ = json.dumps(json_person)

    return (request.json, 200, None)
    # So what we are returning are the json object the status codes and
    # the headers
    # We have to import 'json the use the json dumps to cast the code'


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
