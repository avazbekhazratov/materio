from django.db import models
from materio.models import savdo_oynasi


class shop(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    employee_number = models.IntegerField()
    savdo = models.ForeignKey(savdo_oynasi, on_delete=models.SET_NULL)
    # valyuta = models.CharField(max_length=128, choices=[
    #     ("USD", "USD"),
    #     ("YUAN", "YUAN"),
    #     ("UZS", "UZS")
    # ])
    product_number = models.IntegerField()
