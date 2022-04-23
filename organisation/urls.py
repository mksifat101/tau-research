from django.urls import path
from organisation import views

urlpatterns = [
    path('', views.organisation, name='organisation'),
    path('add/', views.addorg, name='addorg'),
    path('delete/<id>', views.org_delete, name='org_delete'),
    path('activate/<token>/', views.activate, name='activate'),
    path('activated/', views.activated, name='activated'),
]
