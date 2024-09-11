from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users, name='all_users'),
    path('users/', views.all_users, name='all_users'),
    path('users/details/<int:id>', views.details, name='details')
]