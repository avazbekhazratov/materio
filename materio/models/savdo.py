from django.db import models

from materio.models import Maxsulot, User
from materio.models.clent import Client


class savdo_oynasi(models.Model):

    product = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True, blank=True)
    clent_bolsa = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    sotish_narxi = models.CharField(max_length=50)
    valyuta = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])

    def __str__(self):
        return self.product