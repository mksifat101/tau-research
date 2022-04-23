from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('org-portal/', views.org_portal, name='org_portal'),
    path('client-portal/', views.client_portal, name='client_portal'),
]
