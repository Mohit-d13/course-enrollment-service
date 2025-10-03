from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()
mongo_initdb_root_username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
mongo_initdb_root_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
mongo_server = os.getenv("MONGO_SERVER")

mongo_uri = f"mongodb://{mongo_initdb_root_username}:{mongo_initdb_root_password}@{mongo_server}:27017/"

client = MongoClient(mongo_uri, ServerSelectionTimeoutMS=5000)
db = client["studies_db"]
form_collection = db["courses"]

app = Flask(__name__)

@app.route("/")
def root():
    try:
        client.admin.command('ping')
        return "MongoDB connection successfull"
    except ConnectionFailure as e:
        return f"Failed to connect to mongodb database: {e}", 500

@app.route("/submit", methods=["POST"])
def submit():
    print("Backend service activated")
    form_data = request.get_json()
   
    if form_data:
        form_collection.insert_one(form_data)
        return jsonify({"message": "Course enrollment form successfully submitted"}), 200

    return jsonify({"error": "No data received"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)