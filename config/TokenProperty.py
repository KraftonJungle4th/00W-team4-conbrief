from datetime import timedelta


class TokenProperty():
    @staticmethod
    def getMaxAge() -> timedelta:
        return timedelta(minutes=60 * 24)
    
    @staticmethod
    def getSecretKey() -> str:
        return "krafton-jungle-conbrief-team"
    
    @staticmethod
    def getAlgorithm() -> str:
        return "HS256"
