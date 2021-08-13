from django import forms
from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.forms import ProductCategoryForm, ProductForm, ProductCategory
from products.models import Product

class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta():
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class ProductCategoryAdminProfileForm(ProductCategoryForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))


class ProductAdminProfileForm(ProductForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='---► Выберите категорию ◄---')

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')