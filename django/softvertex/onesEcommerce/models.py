from django.db import models


class Products(models.Model):
    category_options = (('electronic', 'Electronic'),
                        ('cosmetic', 'Costmetic'),)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')  
    category = models.CharField(choices=category_options, max_length=50)

    def __str__(self):
        return self.name
