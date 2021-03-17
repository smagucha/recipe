
from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name=''),
   path('favouriterecipe', views.Favoriterecipe, name='favouriterecipe'),
   path('search', views.searchform, name='searchfood'),
 
  
]