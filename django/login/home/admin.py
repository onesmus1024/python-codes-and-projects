from django.contrib import admin
from django.contrib.admin.decorators import display
from django.contrib.admin.helpers import Fieldset
from django.db.models import fields
from .models import User

# Register your models here.
class QuestionAdminView(admin.ModelAdmin):
    """Fieldsets=[
        ('username',{'fields':['username']})
    ]"""
    fields=['username','password']
    list_display=['username','password']
admin.site.register(User,QuestionAdminView)