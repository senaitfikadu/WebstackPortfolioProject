from django.urls import path

from . import views

urlpatterns = [
    path("", views.bookListView),
    path("about", views.about, name="about"),
]