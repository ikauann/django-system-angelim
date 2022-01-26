from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import BlingEstoque


class BlingEstoqueSerializar(serializers.ModelSerializer):

    class Meta:

        model = BlingEstoque
        fields = '__all__'

        def update(self, validated_data):
            print(validated_data)
