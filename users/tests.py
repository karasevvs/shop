from django.test import TestCase
from django.test.client import Client
from users.models import User

# Create your tests here.
STATUS_CODE_ACCESS = 200
STATUS_CODE_REDIRECT = 301
STATUS_CODE_LOGIN_REDIRECT = 302
USERNAME = 'django'
PASSWORD = 'django_qwerty'
EMAIL = 'geek@shop.ru'


class UsersTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(USERNAME, EMAIL, PASSWORD)
        self.client = Client()

    def test_user_login(self):

        # без входа
        response = self.client.get('/')
        self.assertEqual(response.status_code, STATUS_CODE_ACCESS)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertNotContains(response, 'Выйти', status_code=STATUS_CODE_ACCESS)

        # логин
        self.client.login(username=USERNAME, password=PASSWORD)
        response = self.client.get('/users/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        # логин и редирект на главную
        response = self.client.get('/')
        self.assertContains(response, self.user.username, status_code=STATUS_CODE_ACCESS)
        self.assertEqual(response.context['user'], self.user)