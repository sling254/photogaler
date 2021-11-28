from django.urls import path
from .views import IndexView,searched_images,fillter_by_location_Nyeri,fillter_by_location_Nairobi

urlpatterns = [
    path('',IndexView,name="index"),
    path('searched_images',searched_images,name="searched_images"),
    path('fillter_by_location',fillter_by_location_Nyeri,name="fillter_by_location_Nyeri"),
    path('fillter_by_location_nairobi',fillter_by_location_Nairobi,name="fillter_by_location_Nairobi"),
]
