from django.urls import path

from account.views import UserRegisterView, UserLoginView, UserInfoView, UserLogoutView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("user/", UserInfoView.as_view(), name="user"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
