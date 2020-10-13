from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home,name='home'),
    path('show/<int:id>/', views.show, name = 'show'),
    path('search/', views.search_results, name='search_results'),
    path('polygon/',views.polygon, name = 'polygon'),
    path('show/', views.show, name = 'show'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)