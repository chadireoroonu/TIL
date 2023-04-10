from django.shortcuts import render
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    form = ArticleForm()
    return render(request, 'articles/create.html')