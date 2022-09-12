# login/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password
from .serializer import LoginUserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse, JsonResponse



class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        user = LoginUser.objects.filter(user_id=user_id).first()
        if user is None:
            return Response(dict(msg="해당 ID의 사용자가 없습니다."))
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공", user_id=user.user_id, birth_day=user.birth_day,
                                 gender=user.gender, email=user.email, name=user.name, age=user.age))
        else:
            return Response(dict(msg="로그인 실패. 패스워드 불일치"))

            
        
class RegistUser(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(request.data)

        if LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
            # DB에 있는 값 출력할 때 어떻게 나오는지 보려고 user 객체에 담음
            user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first()
            data = dict(
                msg="이미 존재하는 아이디입니다.",
                user_id=user.user_id,
                user_pw=user.user_pw
            )
            return Response(data)
        user = serializer.create(request.data)
        return Response(data=LoginUserSerializer(user).data)


def login_view(request):
    if request.method == 'POST':
        print("request "+ str(request))
        print("body "+ str(request.body))
        userid = request.POST.get("userid", "")
        userpw = request.POST.get("userpw", "")
        user = authenticate(username=userid, password=userpw)

        print("userid = " + userid + " result = " + str(user))
        if user:
            print("로그인성공")
            login(request, user)
        else:
            print("로그인실패")
            return render(request, "login/login.html", status=401)
    return render(request, "login/login.html")

def logout_view(request):
    logout(request)
    return redirect("login:login")

def signup_view(request):
    if request.method == 'POST':
        print("request "+ str(request))
        print("파일 : "+ request.FILES["profile_img"])
        profile_img = request.FILES["profile_img"]
        print("body "+ str(request.body))
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        firstname = request.POST.get("firstname", "")
        lastname = request.POST.get("lastname", "")
        email = request.POST.get("email", "")
        return redirect("login:login")
        
    return render(request, "login/signup.html")
