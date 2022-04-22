from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'foods/index.html')
    # render함수(request, 우리가 원하는 경로)
    # render 함수는 정보와 템플릿을 토대로 하나의 응답 -> 하나의 HttpRespose객체를 만들어 리턴해줌 
    