from django.db import models

from materio.models import Maxsulot


class Storage(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    product_num = models.IntegerField()
    money_type = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    employee_num = models.IntegerField()

    def storges_format(self):
        return {
            "nomi": self.name,
            "location": self.location,
            "product_num": self.product_num,
            "xodim_soni": self.employee_num,
            "money_type": self.money_type
        }

    def __str__(self):
        return self.name


class Storage_order(models.Model):
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    order_number = models.IntegerField()
    sent_number = models.IntegerField()

    def storage_order_format(self):
        return {
            "nomi": self.name,
            "size": self.size,
            "date": self.date,
            "location": self.location,
            "color": self.color,
            "sent_number": self.sent_number,
            "order_number": self.order_number
        }

    def __str__(self):
        return self.name


class OmborMaxsulot(models.Model):
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    ombor = models.ForeignKey(Storage, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ombor}: {self.maxsulot}'

    def save(self, *args, **kwargs):
        return super(OmborMaxsulot, self).save(*args, **kwargs)


class Ombor_buyurtma(models.Model):
    ombor = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True, blank=True)
    order_status = models.CharField(max_length=128, choices=[
        ("Buyurtma qilindi", "Buyurtma qilindi"),
        ("Yig'ilyapti", "Yig'ilyapti"),
        ("Yo'lda", "Yo'lda"),
        ("Keldi", "Keldi")

    ])
    order = models.ForeignKey(Storage_order, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.ombor} : {self.order_status}"
