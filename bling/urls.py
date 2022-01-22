from django.urls import path
from bling import views


urlpatterns = [
    path('estoque', views.BlingEstoqueList.as_view(), name='bling-estoque'),
]
