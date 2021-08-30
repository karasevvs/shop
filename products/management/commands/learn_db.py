from datetime import timedelta

from django.core.management import BaseCommand
from django.db.models import Q, F, When, Case, IntegerField, DecimalField

from products.models import Product
from orderapp.models import OrderItem


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass