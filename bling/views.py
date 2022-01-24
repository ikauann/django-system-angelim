from rest_framework import generics
from .models import BlingEstoque
from .serializers import BlingEstoqueSerializar

#from rest_framework.response import Response
#from rest_framework import status

#from django.http import QueryDict


class BlingEstoqueList(generics.ListCreateAPIView):

    queryset = BlingEstoque.objects.all()
    serializer_class = BlingEstoqueSerializar

    def post(self, request):
    
        print("=========================" * 40)
    
        self.data_post = request.data
        return self.data_post