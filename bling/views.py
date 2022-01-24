from rest_framework import generics
from .models import BlingEstoque
from .serializers import BlingEstoqueSerializar

from rest_framework.response import Response
from rest_framework import status

from django.http import QueryDict

from bibliotecas import tratamento_qj

class BlingEstoqueList(generics.ListCreateAPIView):

    queryset = BlingEstoque.objects.all()
    serializer_class = BlingEstoqueSerializar

    def post(self, request):
        print('=*='*100)
        data_post = request.data
        data_post = dict(data_post)

        data_post_tratado = tratamento_qj(data_post)
        print(data_post_tratado)
        print('=*='*100)

