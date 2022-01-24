from rest_framework import generics
from .models import BlingEstoque
from .serializers import BlingEstoqueSerializar

from rest_framework.response import Response
from rest_framework import status

from django.http import QueryDict

from django.utils import six

class BlingEstoqueList(generics.ListCreateAPIView):

    queryset = BlingEstoque.objects.all()
    serializer_class = BlingEstoqueSerializar

    def post(self, request):
    
        print("=" * 40)
    
        data_post = request.data
        data_post = dict(six.iterlists(data_post))
        print(data_post)
        print(type(data_post))

        print("=" * 40)
