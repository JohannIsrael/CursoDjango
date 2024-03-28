from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home.Home'),
    path('register/', views.view_register, name='register.Home'),
]
