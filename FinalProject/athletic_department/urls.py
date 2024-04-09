from django.urls import path
from . import views


urlpatterns = [
    path('teams/', views.team_list, name='team_list'),
    path('homepage/', views.homepage, name='homepage'),
    # Define other URLs for CRUD operation
]
