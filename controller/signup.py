import bcrypt
from flask import Blueprint, app, redirect, render_template, request, url_for
import jwt
from config.TokenProperty import TokenProperty
from model.Token import Token
from repository.UserRepository import UserRepository
from clientConfigs.onboarding.CONFIGS import SIGN_UP, SIGN_UP_BTN

userRepository = UserRepository()
signup_bp = Blueprint("signup", __name__)


@signup_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('onboarding/signUp.html', CONFIG=SIGN_UP, BTN_CONFIG=SIGN_UP_BTN)

    if request.method == 'POST':
        signupRequestDto = request.form
        if not signupRequestDto['studentNo'] or len(signupRequestDto['password']) < 4 or len(signupRequestDto['passwordCheck']) < 4:
            return render_template('onboarding/signUp.html', CONFIG=SIGN_UP, errorMessage="입력값을 확인해주세요", BTN_CONFIG=SIGN_UP_BTN)

        if signupRequestDto['password'] != signupRequestDto['passwordCheck']:
            return render_template('onboarding/signUp.html', CONFIG=SIGN_UP, errorMessage="두 비밀번호가 일치하지 않습니다.", BTN_CONFIG=SIGN_UP_BTN)

        signupRequestDao = {
            'studentNo': signupRequestDto['studentNo'],
            'password': bcrypt.hashpw(signupRequestDto['password'].encode('utf-8'), bcrypt.gensalt())
        }

        # DB에 수강생정보 저장, 실패시 오류 메세지 반환
        if not userRepository.save(signupRequestDao):
            return render_template('onboarding/signUp.html', CONFIG=SIGN_UP, errorMessage="이미 회원가입이 되어있습니다.")

        # 토큰 발급 후 쿠키 저장
        token = Token(signupRequestDto['studentNo'], TokenProperty.getMaxAge())
        accessToken = jwt.encode(token.toJson(), key=TokenProperty.getSecretKey(
        ), algorithm=TokenProperty.getAlgorithm())

        resp = redirect(url_for('home'))
        resp.set_cookie('accessToken', accessToken, max_age=TokenProperty.getMaxAge(
        ), expires=token.getExpireTime())
        return resp

    raise Exception("지원하지 않는 Method 입니다")
