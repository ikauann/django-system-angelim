from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import BlingEstoque


class BlingEstoqueSerializar(serializers.ModelSerializer):

    sku = serializers.IntegerField(primary_key=True)
    estoque = serializers.CharField(max_length=300)

    class Meta:

        model = BlingEstoque
        fields = '__all__'
