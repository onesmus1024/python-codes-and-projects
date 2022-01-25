from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    description=models.CharField(max_length=200,blank=False,null=False,default='No description provided')
    completed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
