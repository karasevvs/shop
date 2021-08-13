import os
from datetime import datetime
from django.utils import timezone

import requests
from social_core.exceptions import AuthForbidden

from users.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = 'https://api.vk.com/method/users.get'
    fields_tuple = ('bdate', 'sex', 'about', 'has_photo', 'photo_max_orig')
    params = {
        'fields': ','.join(fields_tuple),
        'access_token': response['access_token'],
        'v': '5.92',
    }

    api_response = requests.get(api_url, params=params)
    if api_response.status_code != 200:
        return

    data = api_response.json()['response'][0]

    if data.get('sex'):
        if data['sex'] == 1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE
        if data['sex'] == 2:
            user.shopuserprofile.gender = ShopUserProfile.MALE

    if data.get('about'):
        user.shopuserprofile.aboutMe = data['about']

    if data.get('bdate'):
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        user.birthday = bdate

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.shopuserprofile.age = age

    if data.get('has_photo'):
        file_name = f'ID_{user.id}_photo_vk_id_{data.get("id")}.jpg'
        photo_url = data.get('photo_max_orig')
        result = requests.get(photo_url, stream=True)
        user.image.save(file_name, result.raw)

    if response.get('email'):
        user.email = response['email']

    user.save()




