from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('ajouter/', views.patient_create, name='patient_create'),
    path('modifier/<int:pk>/', views.patient_update, name='patient_update'),
    path('supprimer/<int:pk>/', views.patient_delete, name='patient_delete'),
]