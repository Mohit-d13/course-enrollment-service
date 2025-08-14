from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()
mongodb_uri = os.getenv("MONGODB_URI")

try:
    client = MongoClient(mongodb_uri, ServerSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("MongoDB connection successfull")
except ConnectionFailure as e:
    print(f"Failed to connect to mongodb cluster: {e}")

db = client["flask_mongodb"]
form_collection = db["course"]

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    print("Backend service activated")
    form_data = request.get_json()
   
    if form_data:
        form_collection.insert_one(form_data)
        return jsonify({"message": "Course enrollment form successfully submitted"}), 200

    return jsonify({"error": "No data received"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)