from django.core.management import BaseCommand
from users.models import User, ShopUserProfile

class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.all():
            ShopUserProfile.objects.create(user=user)
        print('create user_profile - DONE')