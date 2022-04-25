from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('org-portal/', views.org_portal, name='org_portal'),
    path('client-portal/', views.client_portal, name='client_portal'),
    path('user/', views.user, name='user'),
    path('user/delete/<id>', views.user_delete, name='user_delete'),
    path('user/edit/<id>', views.user_edit, name='user_edit'),
    path('user/update/<id>', views.user_update, name='user_update'),
    path('org-client/', views.orgclient, name='orgclient'),
]
