from django.urls import path
from orderapp import views

app_name = 'orderapp'

urlpatterns = [
    path('', views.OrderList.as_view(), name='orders_list'),
    path('create/', views.OrderItemCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.OrderItemUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.OrderItemsDelete.as_view(), name='delete'),
    path('read/<int:pk>/', views.OrderItemsRead.as_view(), name='read'),

    path('forming/complete/<int:pk>/', views.order_forming_complete, name='order_forming_complete'),
    path('product/<pk>/price/', views.product_price),
]
