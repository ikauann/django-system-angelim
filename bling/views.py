from rest_framework import generics
from .models import BlingEstoque
from .serializers import BlingEstoqueSerializar

from rest_framework.response import Response
from rest_framework import status

from django.http import QueryDict

#tratar query dict
def tratamento_qj(item):
    item = eval(item['data'][0])
    sku = item['retorno']['estoques'][0]['estoque']['codigo']
    estoque = item['retorno']['estoques'][0]['estoque']['estoqueAtual']
    dicionario = {
        'sku':sku,
        'estoque': estoque
    }
    print(dicionario)

class BlingEstoqueList(generics.ListCreateAPIView):

    queryset = BlingEstoque.objects.all()
    serializer_class = BlingEstoqueSerializar

    def post(self, request):

        print('*='*100)
        data_post = request.data
        data_post = dict(data_post)

        print(data_post)
        print('1 : terminei de rodar')

        #tratamento_qj(data_post)
        #print('=*='*100)

        return Response({"status":"sucess"}, status=status.HTTP_200_OK)
        

