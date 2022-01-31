from django.shortcuts import render
from .serializers import MercadoLivreSerializer
from .models import MercadoLivre
from rest_framework import generics

class MercadoLivreList(generics.ListAPIView):

    queryset = MercadoLivre.objects.all()
    serializer_class = MercadoLivreSerializer

# Create your views here.
