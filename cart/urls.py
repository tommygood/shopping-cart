from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage),
    path('cusMain', views.cusMain),
    path('bossMain', views.bossMain),
]

