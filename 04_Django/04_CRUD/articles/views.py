from django.shortcuts import render, redirect
from .models import Articles

def index(request):
    # ORM
    # class.manater.query API
    articles = Articles.objects.all()
    context = {
        # 특정 단어 or 알파벳 영역 선택 후
        # ctrl + d 하면 같은 단어 다 찾아줌
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    # 특정 게시글 하나 조회
    # 함수 실행 -> article_pk와 pk 값이 동일한 게시글 하나 조회
    article = Articles.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 게시글 생성 요청에 대한 응답
    # 게시글 생성 해주면 역할 끝
    # 진짜 게시글만 만들어주면 UX 문제
    # 게시글 생성 후 특정 페이지를 사용자 반환하도록
    # 다른 요청 경로로 이동

    # 게시글 생성
    article = Articles()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save

    # 다른 요청 경로로 이동
    return redirect('articles:detail', article.pk)

def edit(request, article_pk):
    # class.manage.query API
    article = Articles.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)

def delete(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    article.delete
    return redirect('articles:index')