from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    return render(request, 'articles/create.html')

def profile(request, name):
    # context 이름은 장고가 기본 구조 짤 때 이렇게 썼었음
    context = {
        # key: value
        'name': name
    }
    return render(request, 'articles/profile.html', context)

def info(request, age):
    context = {
        'age': age
    }
    return render(request, 'articles/info.html', context)