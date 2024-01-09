import datetime


class Token():
    """
    studentNo: 수험생 번호
    maxAge: 유효기간 (분단위)
    """
    def __init__(self, studentNo, maxAge) -> None:
        self.__studentNo = studentNo
        self.__exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=maxAge)

    def toJson(self) -> dict:
        return { 'studentNo' : self.__studentNo, 'exp' : self.__exp }
    
    def getExpireTime(self) -> datetime:
        return self.__exp