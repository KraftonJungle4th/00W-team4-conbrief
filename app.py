
from flask import Flask, abort, redirect, render_template, request, url_for

from controller.login import login_bp
from controller.signup import signup_bp
from controller.user import user_bp
from validators import TokenValidator

app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(user_bp)


@app.route('/')
def home():
    return render_template('index.html')


@app.before_request
def filter():
    if request.endpoint == 'static':
        return
    
    # api 인증 처리
    if request.path.startswith("/api"):
        if not request.headers.get('Authorization', None):
            return abort(401)
        
        tokenType, token = request.headers['Authorization'].split()
        try:
            if tokenType != 'Bearer' or TokenValidator.validateToken(token):
                return abort(401)
        except:
            return abort(401)
        
    # 페이지 인증 처리
    if request.path == '/login' and request.cookies.get('accessToken', None):
        return redirect(url_for('home'))
    elif request.path != '/login' and request.path != '/signup' and not TokenValidator.validateAuthReq(request):
        return redirect(url_for('login.login'))
    
