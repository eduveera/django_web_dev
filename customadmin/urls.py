from django.contrib import admin
from django.urls import path,include
from.views import *
from . import views

urlpatterns = [
    path('',admin_login,name='admin_login'),
    path('dashboard/',dashboard, name = 'dashboard'),
    path('logout/', views.admin_logout, name='logout'),
]