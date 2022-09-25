from django.urls import path

from account.views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
]
