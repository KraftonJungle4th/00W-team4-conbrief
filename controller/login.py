import bcrypt
from flask import Blueprint, redirect, render_template, request, url_for
import jwt
from config.TokenProperty import TokenProperty
from model.Token import Token
from repository.UserRepository import UserRepository
from clientConfigs.onboarding.CONFIGS import LOGIN, LOGIN_BTN

userRepository = UserRepository()
login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("onboarding/login.html", CONFIG=LOGIN, BTN_CONFIG=LOGIN_BTN)

    if request.method == 'POST':
        loginRequestDto = request.form
        student = userRepository.findByStudentNo(loginRequestDto['studentNo'])
        if not student or not bcrypt.checkpw(loginRequestDto['password'].encode('utf-8'), student['password']):
            return render_template("onboarding/login.html", CONFIG=LOGIN, errorMessage="아이디, 비밀번호를 확인해주세요", BTN_CONFIG=LOGIN_BTN)

        # 토큰 발급 후 쿠키 저장
        token = Token(loginRequestDto['studentNo'], TokenProperty.getMaxAge())
        accessToken = jwt.encode(token.toJson(), key=TokenProperty.getSecretKey(
        ), algorithm=TokenProperty.getAlgorithm())

        resp = redirect(url_for('home'))
        resp.set_cookie('accessToken', accessToken, max_age=TokenProperty.getMaxAge(
        ), expires=token.getExpireTime())
        return resp

    raise Exception("지원하지 않는 Method 입니다")
