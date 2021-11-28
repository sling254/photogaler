from django.urls import path
from .views import IndexView,searched_images

urlpatterns = [
    path('',IndexView,name="index"),
    path('searched_images',searched_images,name="searched_images"),
]
