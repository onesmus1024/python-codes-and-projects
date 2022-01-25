from django import forms
from django.forms import widgets
from blog.models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['heading','post','posted_by','likes']

        widgets={
            'post':forms.Textarea(attrs={'placeholder':'write your post'}),
            'heading':forms.TextInput(attrs={'placeholder':'post heading'})
        }
