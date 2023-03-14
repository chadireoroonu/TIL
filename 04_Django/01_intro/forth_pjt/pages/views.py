from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'num' : 30
    }
    return render(request,
                  'pages/index.html',
                  context)