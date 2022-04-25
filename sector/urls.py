from django.urls import path
from sector import views

urlpatterns = [
    path('', views.sector, name='sector'),
    path('add/', views.addsector, name='addsector'),
    path('delete/<id>', views.sectordel, name='sectordel'),
    path('edit/<id>', views.sectoredit, name='sectoredit'),
    path('update/<id>', views.sectorupdate, name='sectorupdate'),
]
