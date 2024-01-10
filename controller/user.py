from flask import Blueprint,jsonify, redirect, render_template,request, url_for
import jwt
from config.TokenProperty import TokenProperty
from repository.UserRepository import UserRepository
from clientConfigs.main.CONFIGS import MODYFIABLE_INFO_CONFIG, SEARCH_CONFIG

userRepository =  UserRepository()
user_bp = Blueprint("user", __name__)

@user_bp.route("/api/students/exist/<studentNo>")
def checkStudentNo(studentNo: str):
    return {"exists" : userRepository.existByStudentNo(studentNo=studentNo)}

@user_bp.route("/api/students/infor/<studentNo>")
def getStudentInfor(studentNo:str):

    param = request.args.get('param')
    userInfor = userRepository.findByStudentNo(studentNo=studentNo) 

    if param is None:
        return jsonify(userInfor)
    else:
        return jsonify(userInfor[param])
    
@user_bp.route("/api/students/infor/<studentNo>")
def insertStudentInfor(studentNo:str):

    studentInfor = request.form 
    userRepository.updateStudentInfor(studentInfor,studentNo=studentNo)

@user_bp.route("/mypage", methods=["GET", "POST"])
def mypage():
    token = request.cookies["accessToken"]
    studentNo = jwt.decode(token, TokenProperty.getSecretKey(), TokenProperty.getAlgorithm())["studentNo"]
    student = userRepository.findByStudentNo(studentNo)
    if request.method == "GET":
        result = request.args.get('result', False)
        return render_template("mypage/mypage.html", student=student, MODYFIABLE_INFO_CONFIG=MODYFIABLE_INFO_CONFIG, result=result)
    
    if request.method == "POST":
        updateRequestDto = {} 
        for name, value in request.form.items():
            if value:
                updateRequestDto[name] = value
        userRepository.updateStudentInfor(updateRequestDto, studentNo)
        return redirect(url_for("user.mypage", result=True))








    

    
    




    

    

    

    

