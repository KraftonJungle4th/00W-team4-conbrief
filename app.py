from flask import Flask, redirect, render_template, request, jsonify, url_for
from repository.UserRepository import UserRepository
from clientConfigs.CONFIGS import SIGN_UP

app = Flask(__name__)
userRepository = UserRepository()


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('logIn/signUp.html', CONFIG=SIGN_UP)

    if request.method == 'POST':
        signupRequestDto = request.form
        if not signupRequestDto['studentNo'] or len(signupRequestDto['password']) < 4 or len(signupRequestDto['password-check']) < 4:
            return render_template('logIn/signUp.html', errorMessage="입력값을 확인해주세요")

        if signupRequestDto['password'] != signupRequestDto['password-check']:
            return render_template('logIn/signUp.html', errorMessage="두 비밀번호가 일치하지 않습니다.")

        signupRequestDao = {
            'studentNo': signupRequestDto['studentNo'],
            'password': signupRequestDto['password'],
        }

        # DB에 수강생정보 저장, 실패시 오류 메세지 반환
        if not userRepository.save(signupRequestDao):
            return render_template('logIn/signUp.html', errorMessage="이미 회원가입이 되어있습니다.")

        # 토큰 발급 후 쿠키 저장
        return redirect(url_for('home'))

    raise Exception("지원하지 않는 Method 입니다")
