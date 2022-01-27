from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import BlingEstoque

from rest_framework.response import Response
from rest_framework import status


class BlingEstoqueSerializar(serializers.ModelSerializer):

    class Meta:

        model = BlingEstoque
        fields = '__all__'

    def create(self, validated_data):
        obj, created = BlingEstoque.objects.update_or_create(
        sku=validated_data['sku'], estoque=0, #if sku and estoque equal, update default
        defaults={'estoque':validated_data['estoque']}, #else, create sku and add default 
        )
        return Response({"status":"sucess"}, status=status.HTTP_200_OK)
