from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=50)
    passport = models.CharField(max_length=9)

    def employee_format(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "passport": self.passport
        }

    def __str__(self):
        return self.name

