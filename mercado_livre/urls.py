from django.urls import path
from mercado_livre import views


urlpatterns = [
    path('mercadolivre', views.MercadoLivreList.as_view(), name='bling-estoque'),
]
