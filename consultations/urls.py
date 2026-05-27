from django.urls import path
from . import views

app_name = 'consultations'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('modifier/<int:pk>/', views.update, name='update'),
    path('supprimer/<int:pk>/', views.delete, name='delete'),
    path('ajouter/', views.create, name='ajouter'),
]