from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):

    title = request.GET.get('title')
    content = request.GET.get('content')

    print(title, content)

    # ORM
    # class.manage.queryAPI
    # Article.objects.create()
    
    # 데이터베이스 생성 방법 3
    # 1. article instance 생성하는 방법
    article = Article()


    return render(request, 'articles/create.html')
