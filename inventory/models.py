from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    in_stock = models.BooleanField(default=True)