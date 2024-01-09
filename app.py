from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
db = MongoClient(os.environ.get("MONGO_URI")).conbrief


@app.route('/')
def home():
    return render_template('index.html')