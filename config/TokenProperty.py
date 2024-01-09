class TokenProperty():
    """
    토큰 유효기간(분 단위)
    """
    @staticmethod
    def getMaxAge() -> int:
        return 60 * 24
    
    @staticmethod
    def getSecretKey() -> str:
        return "krafton-jungle-conbrief-team"
    
    @staticmethod
    def getAlgorithm() -> str:
        return "HS256"
