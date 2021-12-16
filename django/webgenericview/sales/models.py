from django.db import models

# Create your models here.

class Electronics(models.Model):
    name = models.CharField(max_length=20)
    item_id = models.PositiveIntegerField()
    product_description = models.CharField(max_length=100)
