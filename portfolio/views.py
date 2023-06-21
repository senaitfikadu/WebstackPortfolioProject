from django.shortcuts import render
from .models import Movie
from django.contrib.auth.decorators import login_required

@login_required
def movieListView(request):
    context = {
        "movie_list":Movie.objects.all()
    }
    return render(request, "home.html", context)
    
@login_required
def about(request):
    return render(request, "about.html")
