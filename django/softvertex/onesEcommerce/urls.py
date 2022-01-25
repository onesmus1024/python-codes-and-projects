from operator import ipow
from django.urls import path
from onesEcommerce import views

app_name ='onesEcommerce'
urlpatterns = [
    path('',views.ProductView.as_view(),name='products'),
    path('add',views.ProductsCreateView.as_view(),name='addProduct'),
]
