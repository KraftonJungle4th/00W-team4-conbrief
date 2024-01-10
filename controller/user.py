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
    receivedData = request.get_json()
    
    #점수
    correctNum = receivedData["correctNum"]
    
    #검색된 사람
    searchedNo = receivedData["searchNo"]
    searchedData = userRepository.findByStudentNo(searchedNo) #dictionary 
    
    #문제 푼 사람
    token = request.headers.get("Authorization").split()[1]
    payload = jwt.decode(token, key=TokenProperty.getSecretKey(), algorithms=[TokenProperty.getAlgorithm()])
    searcherNo = payload["studentNo"]
    searcherData = userRepository.findByStudentNo(searcherNo)
    

    #ratedFriends 당한 사람 data에 들어가는것
    userRepository.insertRatedFriend(searcherNo=searcherNo,
                                    searchedNo=searchedNo
                                    )
    
    #correctRate 삽입
    userRepository.insertCorrectRate(searcherNo=searcherNo,
                                    correctNum=correctNum
                                    )
    
    #friendlyRate