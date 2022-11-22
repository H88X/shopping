from django import forms
from shop.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'author', 'name', 'description', 'stock', 'price']


class ImageUploadForm(forms.Form):
    image = forms.ImageField()






