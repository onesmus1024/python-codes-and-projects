from django import forms
from onesEcommerce.models import Products


class ProductsForm(forms.ModelForm):
    
    class Meta:
        model = Products
        fields = ('name','description','image','category')
