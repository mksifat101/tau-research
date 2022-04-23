from django.urls import path
from client import views

urlpatterns = [
    path('', views.client, name='client'),
    path('add/', views.addclient, name='addclient'),
]
