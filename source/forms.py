from django import forms
from django.forms import widgets
from source.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'picture']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control mb-3',
                                              'placeholder': 'Название'}),
            'category': widgets.Select(attrs={'class': 'form-control mb-3'}),
            'description': widgets.Textarea(attrs={'class': 'form-control mb-3'}),
            'picture': widgets.ClearableFileInput(attrs={'class': 'form-control mb-3'})
        }