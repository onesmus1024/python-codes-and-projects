from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest,HttpResponseRedirect
from django.urls import reverse
from .models import User
# Create your views here.

class IndexView(generic.ListView):
    model=User
    template_name = 'home/index.html'


class SignUp(generic.DetailView):
    pass   

def signup(request):
    
    #return HttpResponse(render(request,'home/success.html'))
    return HttpResponseRedirect('/thank')
