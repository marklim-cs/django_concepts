from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users, name='all_users'),
    path('users/', views.all_users, name='all_users'),
    path('users/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]