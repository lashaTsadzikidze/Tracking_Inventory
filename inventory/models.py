from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    serialNumber = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return self.name