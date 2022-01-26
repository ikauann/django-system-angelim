from django.db import models


class BlingEstoque(models.Model):

    objects = models.Manager()

    sku = models.CharField(max_length=300)
    estoque = models.CharField(max_length=300)
