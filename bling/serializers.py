from rest_framework import serializers
from .models import BlingEstoque
from rest_framework.response import Response


class BlingEstoqueSerializar(serializers.ModelSerializer):

    class Meta:

        model = BlingEstoque
        fields = '__all__'

    def fb_credits_callback(request):
        # parse with your parse function
        # handle request
        return HttpResponse(json.dumps(data))