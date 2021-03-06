from rest_framework import generics
from .models import BlingEstoque
from .serializers import BlingEstoqueSerializar

from rest_framework.response import Response
from rest_framework import status

from django.http import QueryDict

#tratar query dict
def tratamento_qj(items):
    dicts = []
    items = eval(items['data'][0])
    for item in items['retorno']['estoques']:    
        sku = item['estoque']['codigo']
        estoque = item['estoque']['estoqueAtual']
        
        dicionario = {
            'sku':sku,
            'estoque': estoque
        }
        dicts.append(dicionario)
    return dicts

class BlingEstoqueList(generics.ListCreateAPIView):

    queryset = BlingEstoque.objects.all()
    serializer_class = BlingEstoqueSerializar

    def post(self, request):

        data_post = request.data
        data_post = dict(data_post)

        updates = []
        for produto in tratamento_qj(data_post):
            updates.append(produto)

            BlingEstoqueSerializar.create(self, validated_data=produto)

        return Response({"status":"sucess"}, status=status.HTTP_200_OK)
        

