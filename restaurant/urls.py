"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 새로운 URL 추가 위하여 include 함수 추가 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', include('foods.urls')),
    path('', include('foods.urls') ),
    path('menus/', include('menus.urls')),
    # include 함수를 쓰기 위해서는 django.urls로부터 include 함수 가져와야함 
    # 만약 주소에 foods가 있으면 foods 앱 안의 urls.py 파일을 보라고 알려줌 
    # 이를 위하여 food 디렉토리 내 urls.py 생성해줘야 함 
]
