
from datetime import datetime, timedelta
from flask import Flask, make_response, redirect, render_template, request, jsonify, url_for
from config.TokenProperty import TokenProperty
from model.Token import Token
from repository.UserRepository import UserRepository
import bcrypt
import jwt

app = Flask(__name__)
userRepository =  UserRepository()

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('sign-up-form.html')
    
    if request.method == 'POST':
        signupRequestDto = request.form
        if not signupRequestDto['studentNo'] or len(signupRequestDto['password']) < 4 or len(signupRequestDto['password-check']) < 4:
            return render_template('sign-up-form.html', errorMessage="입력값을 확인해주세요")
        
        if signupRequestDto['password'] != signupRequestDto['password-check']:
            return render_template('sign-up-form.html', errorMessage="두 비밀번호가 일치하지 않습니다.")
        
        signupRequestDao = {
            'studentNo' : signupRequestDto['studentNo'],
            'password' : bcrypt.hashpw(signupRequestDto['password'].encode('utf-8'), bcrypt.gensalt())
        }

        # DB에 수강생정보 저장, 실패시 오류 메세지 반환
        if not userRepository.save(signupRequestDao):
            return render_template('sign-up-form.html', errorMessage="이미 회원가입이 되어있습니다.")

        # 토큰 발급 후 쿠키 저장
        token = Token(signupRequestDto['studentNo'], 1)
        accessToken = jwt.encode(token.toJson(), key=TokenProperty.getSecretKey(), algorithm=TokenProperty.getAlgorithm())

        resp = redirect(url_for('home'))
        resp.set_cookie('accessToken', accessToken, max_age=TokenProperty.getMaxAge(), expires=token.getExpireTime())
        return resp

    raise Exception("지원하지 않는 Method 입니다")

