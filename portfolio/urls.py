from django.urls import path

from . import views

urlpatterns = [
    path("", views.movieListView),
    path("about", views.about, name="about"),
]