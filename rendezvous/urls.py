from django.urls import path
from . import views

app_name = 'rendezvous'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('ajouter/', views.ajouter, name='ajouter'),
    path('modifier/<int:pk>/', views.modifier, name='modifier'),
    path('supprimer/<int:pk>/', views.supprimer, name='supprimer'),
]