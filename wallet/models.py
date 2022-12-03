from django.db import models

# Create your models here.
class Wallet(models.Model):
    def __str__(self):
        return self.name
    price = models.FloatField()