from materio.models.auth import User
from django.db import models


class Maxsulot(models.Model):
    product_name = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    joyi = models.CharField(max_length=128)
    soni = models.IntegerField()
    product_price = models.IntegerField(default=0)
    product_price_type = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    entry_price = models.IntegerField(default=0)
    entry_price_type = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])

    def prod_format(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "size": self.size,
            "color": self.color,
            "joyi": self.joyi,
            "soni": self.soni,
            "product_price": self.product_price,
            "entry_price": self.entry_price
        }


    def __str__(self):
        return self.product_name


class chetdan_buyurtma(models.Model):
    shartnome_raqami = models.IntegerField()
    davlat_nomi = models.CharField(max_length=128)
    zavod_nomi = models.CharField(max_length=128)
    date = models.DateField()
    holati = models.CharField(max_length=128, choices=[
        ("tuzildi", "tuzildi"),
        ("yakunlandi", "yakunlandi"),
        ("yolda", "yolda"),
        ("qabul_qilindi", "qabul_qilindi")
    ])
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.SET_NULL, null=True, blank=True)

    def chetdan_buyurtma_format(self):
        return {
            "id": self.id,
            "shartnoma_raqami": self.shartnome_raqami,
            "davlat_nomi": self.davlat_nomi,
            "zavod_nomi": self.zavod_nomi,
            "date": self.date,
            "holati": self.holati
        }

    def __str__(self):
        return self.shartnome_raqami


class Basket(models.Model):
    product = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quent = models.IntegerField(default=1)
    price = models.BigIntegerField(default=0)
    price_type = models.CharField(max_length=128, choices=[
        ("USD", "USD"),
        ("YUAN", "YUAN"),
        ("UZS", "UZS")
    ])
    status = models.BooleanField(default=True)

    def format(self):
        return {
            "product": self.product.product_name,
            "quent": self.quent,
            "price": self.price,
            "price_type": self.price_type
        }

    def save(self, *args, **kwargs):
        self.price = int(self.product.product_price) * int(self.quent)
        self.price_type = f"{self.product.product_price_type}"

        return super(Basket, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}: {self.product}"


class Basket_order(models.Model):
    basket_name = models.CharField(max_length=128)
    order_num = models.BigAutoField(primary_key=True)
    order_condation = models.IntegerField(default=0)
