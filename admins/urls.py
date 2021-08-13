from django.urls import path
from admins.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryListView, \
    CategoryUpdateView, CategoryDeleteView, CategoryCreateView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),

    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('category/remove/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_remove'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),

    path('products/', ProductListView.as_view(), name='admin_product'),
    path('products/create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products/remove/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_remove'),
]
