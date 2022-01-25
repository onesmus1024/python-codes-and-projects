from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    #custom model manager
    ###################################################
    # class PostManager(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(pk=2)
    ###################################################
    
    heading = models.CharField(max_length=100,blank=False)
    post = models.TextField( max_length=1000)
    posted_by =models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    last_updated = models.DateField( auto_now_add=True)
    date_posted = models.DateField( auto_now_add=True)
    likes=models.IntegerField(blank=False,null=False)
#########################################
    # PostsManager = PostManager()
    objects=models.Manager()
########################################
    def __str__(self):
        return self.heading


    
