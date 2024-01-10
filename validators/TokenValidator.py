import jwt

from config.TokenProperty import TokenProperty


def validateAuthReq(request):
    if not request.cookies.get('accessToken', None): return False;
    token = request.cookies.get('accessToken')

    try:
        jwt.decode(token, key=TokenProperty.getSecretKey(), algorithms=[TokenProperty.getAlgorithm()])
        return True
    except:
        return False
    
def validateToken(token):
    try:
        jwt.decode(token, key=TokenProperty.getSecretKey(), algorithms=[TokenProperty.getAlgorithm()])
        return True
    except:
        return False