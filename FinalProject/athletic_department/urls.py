from django.urls import path, include
from . import views
from .views import TeamCreateView,TeamUpdateView,TeamDeleteView


urlpatterns = [
    path('teams/', views.team_list, name='team_list'),

    path('teams/create/', TeamCreateView.as_view(), name='team_create'),
    path('teams/<int:pk>/update/', TeamUpdateView.as_view(), name='team_update'),
    path('teams/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),

    path('homepage/', views.homepage, name='homepage'),

    #path('add_employee/', views.add_employee, name='add_employee'),

    # Define other URLs for CRUD operation
]


