from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Electronics

# Create your views here.
def index(request):
    return render(request,'sales/index.html')

class index1(generic.ListView):
    model = Electronics
    template_name='sales/index.html'