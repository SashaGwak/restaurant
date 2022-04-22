# foods 파일 내 URL 지정 
from django.contrib import admin
from django.urls import path
# 여기서는 include 필요 없어서 지움 
from . import views

urlpatterns = [
    path('index/', views.index),
    # 이 foods 앱 안의 views.py를 보라는 의미
    # views 사용하기 위해서 import 해줘야함(veiws 모듈에서 index함수 가져오도록)
    # views.py에서 HttpResponse 사용하여 index 함수 지정해줘야함 
]