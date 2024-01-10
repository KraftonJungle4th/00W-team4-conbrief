import os
from pymongo import MongoClient

class UserRepository:
    def __init__(self):
        if os.environ.get("MONGO_URI"):
            self.__db = MongoClient(os.environ.get("MONGO_URI")).conbrief.users
            return
        self.__db = MongoClient("127.0.0.1").conbrief.users

    def save(self, signupRequestDto: dict) -> bool:
        assert signupRequestDto["studentNo"]
        if self.__db.find_one({"studentNo": signupRequestDto['studentNo']}):
            return False

        self.__db.insert_one(signupRequestDto)   
        return True
    
    def existByStudentNo(self, studentNo: str) -> bool:
        return True if self.__db.find_one({"studentNo": studentNo}) else False
    
    def findByStudentNo(self, studentNo: str) -> dict:
        student = self.__db.find_one({"studentNo": studentNo})
        return student
    
    def updateStudentInfor(self,studentInforDto:dict,studentNo:str):
        
        self.__db.update_one({"studentNo":studentNo},{'$set':studentInforDto})



    def insertRatedFriend(self,searcherNo:str,searchedNo:str):
        # if not "ratedFriend" in searchedData:
            self.__db.update_one({"studentNo":searchedNo},{"$set":{"ratedFriend":searcherNo}},upsert=True)
            
        
    
    def insertCorrectRate(self,searcherNo:str,correctNum:int):
        # if not "correctRate" in searcherData:
            self.__db.update_one({"studentNo":searcherNo},{"$set":{"correctRate":correctNum}},upsert=True)
            

    


