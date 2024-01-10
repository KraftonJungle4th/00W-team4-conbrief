from flask import Blueprint,jsonify,request,template_rendered
from repository.UserRepository import UserRepository
from clientConfigs.main.CONFIGS import SEARCH_CONFIG
from config.TokenProperty import TokenProperty
import jwt


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

@user_bp.route("/api/game/data")
def updateGameResultData():
    receivedData = request.form

    searchedNo = receivedData["searchNo"]
    searchedData = userRepository.findByStudentNo(searchedNo)


    

        
    
    searchNo = jwt.decode(token, key=TokenProperty.getSecretKey(), algorithms=[TokenProperty.getAlgorithm()])
    
    correctNum = receivedData["correctNum"]












    

    
    




    

    

    

    

