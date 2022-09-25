from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        username: str,
        company_name: str,
        password: str = None,
        is_staff: bool = False,
        is_superuser: bool = False,
    ) -> "User":
        if not email:
            raise ValueError("이메일은 필수입니다.")
        if not username:
            raise ValueError("이름은 필수입니다.")
        if not company_name:
            raise ValueError("회사명은 필수입니다.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            company_name=company_name,
        )

        user.set_password(raw_password=password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(
        self, email: str, username: str, company_name: str, password: str = None
    ) -> "User":
        user = self.create_user(
            email=email,
            username=username,
            company_name=company_name,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(raw_password=password)
        user.save()
        return user


class User(AbstractUser):
    first_name = None
    last_name = None

    email = models.EmailField(verbose_name="이메일", unique=True)
    username = models.CharField(verbose_name="이름", max_length=12)
    company_name = models.CharField(verbose_name="회사명", max_length=25)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "company_name"]

    objects = UserManager()
