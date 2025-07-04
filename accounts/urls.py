from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.show_register, name='show_register'),
    path('user_register', views.user_register, name='user_register'),
    path('login', views.show_login, name='login'),
    path('user_login', views.user_login ,name='user_login'),
    path('logout', views.logout, name='logout')
]