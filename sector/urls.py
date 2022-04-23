from django.urls import path
from sector import views

urlpatterns = [
    path('', views.sector, name='sector'),
    path('add/', views.addsector, name='addsector'),
    path('delete/<id>', views.sectordel, name='sectordel'),
]
