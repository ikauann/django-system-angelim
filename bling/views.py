from rest_framework import generics
from .models import BlingEstoque
from .serializers import BlingEstoqueSerializar


class BlingEstoqueList(generics.ListCreateAPIView):

    queryset = BlingEstoque.objects.all()
    serializer_class = BlingEstoqueSerializar
