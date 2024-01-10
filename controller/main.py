import bcrypt
from flask import Blueprint, app, redirect, render_template, request, url_for
import jwt
from config.TokenProperty import TokenProperty
from model.Token import Token
from repository.UserRepository import UserRepository
from clientConfigs.main.CONFIGS import SEARCH_CONFIG, INFO_CONFIG, GAME_BTN_CONFIG

userRepository = UserRepository()
main_bp = Blueprint("main", __name__)


@main_bp.route("/main", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main/main.html', SEARCH_CONFIG=SEARCH_CONFIG)

    if request.method == 'POST':
        studentNo = request.form["searchNo"]
        RESULT = userRepository.findByStudentNo(studentNo=studentNo)
        necesskeys=["age","mbti","ttfTruth1","ttfTruth2","ttfFalse"]

        if all((key in RESULT) for key  in necesskeys):
            buttonActivate = True
        else:
            buttonActivate = False
            
        
        return render_template('main/main.html',
                            SEARCH_CONFIG = SEARCH_CONFIG,
                            RESULT = RESULT,
                            INFO_CONFIG=INFO_CONFIG,
                            GAME_BTN_CONFIG=GAME_BTN_CONFIG,
                            HAS_GAME = buttonActivate
                            )
