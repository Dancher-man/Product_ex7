from django import forms
from django.forms import widgets
from source.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'picture']
        widgets = {'description': widgets.Textarea, 'category': widgets.CheckboxInput}