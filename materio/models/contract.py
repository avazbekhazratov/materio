from django.db import models

from magazin.models import Product


class Contract(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_number = models.IntegerField(default=1)
    product_date = models.DateField()


class Contract_item(models.Model):
    contract_id = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        self.total = self.product.sale_price * self.quantity
        return super(Contract_item, self).save(*args, **kwargs)