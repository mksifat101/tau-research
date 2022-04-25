from django.urls import path
from client import views

urlpatterns = [
    path('', views.client, name='client'),
    path('add/', views.addclient, name='addclient'),
    path('delete/<id>/', views.client_delete, name='client_delete'),
    path('edit/<id>/', views.client_edit, name='client_edit'),
    path('update/<id>/', views.client_update, name='client_update'),
    path('activate/<token>/', views.clientactivate, name='clientactivate'),
    path('activated/', views.clientactivated, name='clientactivated'),
]
