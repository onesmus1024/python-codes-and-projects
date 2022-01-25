from django.db import router
from django.http.response import HttpResponse
from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets,permissions


# Create your views here.


def index(request):
    #return HttpResponse("<h1>this is api test<h1/>")
    return render(request=request,template_name='api/index.html')

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


    