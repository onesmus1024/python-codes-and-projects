from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=1000)
    registration_date=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.username



