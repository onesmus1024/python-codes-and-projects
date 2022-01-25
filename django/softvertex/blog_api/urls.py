from django.urls import path
from blog_api import views

app_name ='blog_api'
urlpatterns = [
    path('post/',views.PostApiView.as_view(),name='postview'),
    path('user/',views.UserCreate.as_view(),name='registeruser'),
    path('update/<int:pk>/',views.update_post,name='updatepost'),
    path('get/<int:pk>/',views.get_post,name='getpost'),
    path('getwithclass/<int:pk>',views.SinglePost.as_view(),name='getpostwithclass'),
    path('view',views.PostApiView.as_view(),name='api')
]
