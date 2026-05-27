from django.urls import path
from . import views

app_name = 'medecins'

urlpatterns = [
    path('', views.medecin_list, name='medecin_list'),
    path('ajouter/', views.medecin_create, name='medecin_create'),
    path('modifier/<int:pk>/', views.medecin_update, name='medecin_update'),
    path('supprimer/<int:pk>/', views.medecin_delete, name='medecin_delete'),
    path('detail/<int:pk>/', views.medecin_detail, name='medecin_detail'),
]