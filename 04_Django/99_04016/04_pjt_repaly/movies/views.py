from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'GET':
        form = MovieForm
    
    else:
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')

    context = {'form':form}
    return render(request, 'movies/create.html', context)


