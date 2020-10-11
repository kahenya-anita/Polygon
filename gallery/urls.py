from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('search/', views.search_results, name='search_results'),
    path('image/(<image_id>\d+)',views.image,name ='image'),
    path('category/(<category_id>\d+)',views.category,name ='category'),
    path('location/(<location_id>\d+)',views.location,name ='location'),
]