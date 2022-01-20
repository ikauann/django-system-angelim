from django.contrib import admin
from django.urls import path, include
from bling import views

urlpatterns = [
    path('estoque', views.BlingEstoqueList.as_view(), name='bling-estoque'),
]