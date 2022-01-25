from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from flask_login import login_required
from rest_framework import generics,permissions
from blog_api.serializers import PostSerializer,UserSerializer
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['PUT'])
def update_post(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='PUT':
        serialzer = PostSerializer(post,data=request.data)
        data={}
        if serialzer.is_valid():
            serialzer.save()
            data["success"]="updated successfully"
            return Response(data=data)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
####################################################################################
#functional api view
@api_view(['GET'])
def get_post(request,pk):
    try:
        post = Post.objects.get(pk=pk)
        print(pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialzer = PostSerializer(post,)
        return Response(serialzer.data)

####################################################################################
class SinglePost(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer


#####################################################################
#testing custom model manager
class PostApiView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_class =[permissions.IsAuthenticatedOrReadOnly]
######################################################################


class UserCreate(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
