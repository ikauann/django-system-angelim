from .models import MercadoLivre
from rest_framework import serializers


class MercadoLivreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MercadoLivre
        field = "__all__"