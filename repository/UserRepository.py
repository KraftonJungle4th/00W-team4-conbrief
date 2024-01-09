from pymongo import MongoClient


class UserRepository:
    def __init__(self):
        self.__db = MongoClient("127.0.0.1").conbrief.user

    def save(self, signupRequestDto: dict):
        assert signupRequestDto["studentNo"]
        if self.__db.find_one({"studentNo": signupRequestDto['studentNo']}):
            return False

        self.__db.insert_one(signupRequestDto)   
        return True
