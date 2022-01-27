from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import BlingEstoque


class BlingEstoqueSerializar(serializers.ModelSerializer):

    class Meta:

        model = BlingEstoque
        fields = '__all__'

    def create(self, validated_data):
        obj, created = BlingEstoque.objects.update_or_create(
        sku=0, estoque='Lennon',
        defaults={'estoque': validated_data['sku']},
        )
