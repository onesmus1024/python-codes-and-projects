from django.shortcuts import render
from django.http import request,HttpResponseRedirect
from blog.forms import PostForm
from blog.models import Post

def index(request):
    return render(request,'blog/home.html')

def create_post(request):

    if request.method == 'POST':
        post= PostForm(request.POST)
        if post.is_valid:
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm
        context ={}
        context['form'] = form
        return render(request,'blog/add_post.html',context)
        



