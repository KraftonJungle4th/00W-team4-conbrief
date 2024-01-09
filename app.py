from flask import Flask, render_template

from controller.login import login_bp
from controller.signup import signup_bp
from controller.user import user_bp

app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(user_bp)


@app.route('/')
def home():
    return render_template('index.html')
