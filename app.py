from flask import Flask, redirect, render_template, request, jsonify, url_for
from repository.UserRepository import UserRepository

app = Flask(__name__)

userRepository =  UserRepository()

@app.route('/')
def home():
    return render_template('index.html')