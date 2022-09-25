from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from django_rest_auth import settings

from account import services
from account.models import User
from account.authentication import CustomAuthentication
from account.serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserInfoSerializer,
)

import datetime
import jwt


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.instance = User.objects.create_user(**serializer.data)

        return Response(data="register success", status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = services.get_user_email(**serializer.validated_data)

        payload = dict(
            id=user.id,
            exp=datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            iat=datetime.datetime.utcnow(),
        )

        token = jwt.encode(
            payload=payload, key=settings.JWT_SECRET_KEY, algorithm="HS256"
        )

        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = "Login success"
        response.status_code = status.HTTP_200_OK

        return response


class UserInfoView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        serializer = UserInfoSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


class UserLogoutView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = "logout success"
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
