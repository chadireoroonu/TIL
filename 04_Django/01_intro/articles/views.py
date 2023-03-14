from django.shortcuts import render

# Create your views here.
# view 함수의 첫 인자는 반드시 request
def index(request):
    context = {
        'num': 30
    }
    return render(request,
                  'articles/index.html',
                  context)
