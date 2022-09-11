# login/urls.py
from django.urls import path
from .views import RegistUser, AppLogin, login_view, logout_view, signup_view

app_name = "login"

urlpatterns = [
    path('regist_user', RegistUser.as_view(), name='regist_user'),
    path('app_login', AppLogin.as_view(), name='app_login'),
    path('login', login_view, name='login'),
    path('logout',logout_view, name='logout'),
    path('signup',signup_view,name='signup'),
]