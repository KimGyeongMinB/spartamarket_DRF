from django.core.validators import validate_email
from .models import User

# 회원가입 vaildators
def validate_signup(signup_data):
    username = signup_data.get("username")
    password = signup_data.get("password")
    nickname = signup_data.get("nickname")
    birthday = signup_data.get("birthday")
    first_name = signup_data.get("first_name")
    last_name = signup_data.get("last_name")
    email = signup_data.get("email")
    # introduce = signup_data.get("introduce")
    gender = signup_data.get("gender")

    if User.objects.filter(username=username).exists():
        return False, "동일한 username이 있습니다."

    if len(nickname) > 10:
        return False, "닉네임은 10자 까지입니다."

    # 이메일 형식 검사
    try:
        validate_email(email)
    except:
        return False, "email 형식이 올바르지 않습니다."

    if User.objects.filter(email=email).exists():
        return False, "동일한 email 이 있습니다."
    
    return True, ""

#################################################################

def validate_update_user(user_data):
    username = user_data.get("username")
    nickname = user_data.get("nickname")
    birthday = user_data.get("birthday")
    email = user_data.get("email")
    # password = user_data.get("password")

    if User.objects.filter(email=email).exists():
        return False, "동일한 email 이 있습니다."
    
    if len(nickname) > 10:
        return False, "닉네임은 10자 까지입니다."
    
    if len(nickname) <= 0:
        return False, "닉네임이 비어 있습니다."
    
    if len(birthday) <= 0:
        return False, "닉네임이 비어 있습니다."
    
    if len(username) <= 0:
        return False, "닉네임이 비어 있습니다."
    
    # if User.objects.filter(password != password).exists():
    #     return False, "password는 비밀번호 변경 페이지 에서 바꿔주시길 바랍니다"

    return True, ""