from django.db import models


class MercadoLivre(models.Model):

    mlb = models.CharField(primary_key=True, max_length=200)
    estoque = models.IntegerField()
    conta = models.CharField(max_length=10)
    criacao = models.CharField(max_length=60)
    preco = models.FloatField()
    qnd_vendidas = models.IntegerField()
    sku = models.CharField(max_length=20)
    titulo = models.CharField(max_length=60)
    visitas = models.IntegerField()
    status = models.CharField(max_length=20)
    status_updates = models.CharField(max_length=20)
    status_info = models.CharField(max_length=20)
    status_visitas = models.CharField(max_length=20)
    
