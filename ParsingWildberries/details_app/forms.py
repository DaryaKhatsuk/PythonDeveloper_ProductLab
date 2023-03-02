from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    article = forms.CharField(label='Article', max_length=2048)

    class Meta:
        model = Product
        fields = ('article',)
