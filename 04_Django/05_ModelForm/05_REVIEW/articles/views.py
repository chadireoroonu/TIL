from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 모든 게시글 조회
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'articles/index.html')

# GET /articles/create/  | 게시글 생성 페이지 조회
# POST /articles/create/ | 게시글 생성을 위해 DB에 저장
def create(request):
    # 사용자가 접근한 method에 따라 조건 분기
    # POST 처리
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # POST /articles/create/ -> 게시글 생성하면 본인 역할 끝
            return redirect('articles:index')
    else:
        # GET 처리
        form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, 'articles/create.html', context)
    
def detail(request, article_pk):
    # 게시글 하나 조회
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)