from django.contrib import admin
from django.db.models import fields
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields=['heading','post','posted_by','likes']
    list_display=['heading','last_updated','date_posted','posted_by','likes']

