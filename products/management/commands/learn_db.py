from datetime import timedelta

from django.core.management import BaseCommand
from django.db.models import Q, F, When, Case, IntegerField, DecimalField

from products.models import Product
from orderapp.models import OrderItem


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = Product.objects.filter(
        Q(category__name='офис') | Q(category__name='дом')
        )
        print(products_list.values_list('category__name', flat=True))