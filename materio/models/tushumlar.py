from django.db import models


class Kassa(models.Model):
    date = models.DateTimeField(auto_now=True)
    product_name = models.CharField(max_length=128)
    magazin_name = models.CharField(max_length=128)
    summa = models.IntegerField(max_length=128)
    summa_type = models.CharField(max_length=50)