from django import forms
from products.models import ProductCategory, Product
from django.contrib.auth.forms import UserChangeForm

class ProductCategoryForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}), decimal_places=2)
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity')