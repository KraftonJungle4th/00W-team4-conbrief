from flask import Blueprint,jsonify,request
from repository.UserRepository import UserRepository

userRepository =  UserRepository()
user_bp = Blueprint("user", __name__)

@user_bp.route("/api/students/exist/<studentNo>")
def checkStudentNo(studentNo: str):
    return {"exists" : userRepository.existByStudentNo(studentNo=studentNo)}

@user_bp.route("/api/students/infor/<studentNo>") #학생 정보 제공
def getStudentInfor(studentNo:str):

    param = request.args.get('param')
    userInfor = userRepository.findByStudentNo(studentNo=studentNo) 

    if param is None:
        return jsonify(userInfor)
    else:
        return jsonify(userInfor[param])
    
@user_bp.route("/api/students/infor/<studentNo>")
def insertStudentInfor(studentNo:str):

    studentInfor = request.form #dict data 저장
    userRepository.saveStudentInfor(studentInfor,studentNo=studentNo)



    


    
    




    

    

    

    

