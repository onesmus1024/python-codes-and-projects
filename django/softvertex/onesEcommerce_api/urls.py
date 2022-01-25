from django.urls import path 
from onesEcommerce_api import views

app_name='onesEcommerce_api'
urlpatterns = [
    path('',views.ProductViewApi.as_view(),name='productapi')
]
