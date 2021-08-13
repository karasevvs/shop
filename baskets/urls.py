from django.urls import path

from baskets.views import basket_add, basket_remove, basket_edit, view

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:id>/', basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
    path('view/', view, name='view'),
]
