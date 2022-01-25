from operator import imod
from django.shortcuts import render
from django.views import generic
from onesEcommerce.models import Products
from onesEcommerce.forms import ProductsForm

class ProductView(generic.ListView):
    model = Products
    template_name='onesEcommerce/products.html'
    # def get_queryset(self):
    #     products= super().get_queryset()
    #     products = Products.objects.all()
    

class ProductsCreateView(generic.CreateView):
    model = Products
    template_name = "onesEcommerce/addProduct.html"
    form_class=ProductsForm
    success_url = '../products'

    