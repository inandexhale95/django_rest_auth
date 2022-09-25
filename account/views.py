from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import UserRegisterSerializer
from account.models import User


class UserRegisterView(APIView):
    def post(self, request):
        register_serializer = UserRegisterSerializer(data=request.data)
        register_serializer.is_valid(raise_exception=True)

        register_serializer.instance = User.objects.create_user(
            **register_serializer.data
        )

        return Response(data="register success", status=status.HTTP_201_CREATED)
