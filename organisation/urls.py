from django.urls import path
from organisation import views

urlpatterns = [
    path('', views.organisation, name='organisation'),
    path('add/', views.addorg, name='addorg'),
    path('delete/<id>', views.org_delete, name='org_delete'),
    path('edit/<id>', views.org_edit, name='org_edit'),
    path('update/<id>', views.org_update, name='org_update'),
    path('activate/<token>/', views.activate, name='activate'),
    path('activated/', views.activated, name='activated'),
]
