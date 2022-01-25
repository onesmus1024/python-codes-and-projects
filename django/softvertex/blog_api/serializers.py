from django.db.models import fields
from rest_framework import serializers,permissions
from blog.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['heading','post','likes','id','date_posted']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','is_active']