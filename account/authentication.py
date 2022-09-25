from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from account.models import User

from django_rest_auth import settings

import jwt


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return None

        try:
            payload = jwt.decode(
                jwt=token, key=settings.JWT_SECRET_KEY, algorithms=["HS256"]
            )
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = User.objects.filter(id=payload.get("id")).first()

        return (user, None)
