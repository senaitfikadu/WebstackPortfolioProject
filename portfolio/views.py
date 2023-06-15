from django.shortcuts import render
from .models import Movie


def bookListView(request):
    context = {
        "movie_list":Movie.objects.all()
    }
    return render(request, "home.html", context)
    

def about(request):
    return render(request, "about.html")
