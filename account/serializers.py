from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, min_length=2, max_length=12)
    company_name = serializers.CharField(required=True, min_length=2, max_length=25)
    password = serializers.CharField(required=True, min_length=6)
    confirm_password = serializers.CharField(
        required=True, write_only=True, min_length=6
    )

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("confirm_password"):
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return attrs

    # def to_internal_value(self, data):
    #     data = super().to_internal_value(data)
    #
    #     return UserDataclass(**data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
