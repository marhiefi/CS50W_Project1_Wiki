from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("wiki/<str:entry>", views.entry, name="entry"),
    path("wiki/<str:title>", views.title, name="title"),
    path("search/", views.search, name="search")
]
