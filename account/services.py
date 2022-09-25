from rest_framework.exceptions import AuthenticationFailed

from account.models import User


def get_user_email(email: str, password: str) -> "User":
    user = User.objects.filter(email=email).first()

    if user is None:
        raise AuthenticationFailed("이메일에 해당하는 유저가 없습니다.")

    if not user.check_password(raw_password=password):
        raise AuthenticationFailed("비밀번호가 틀렸습니다.")

    return user
