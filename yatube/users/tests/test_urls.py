from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from http import HTTPStatus

User = get_user_model()

class UserPagesURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test_author')

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='HasNoName')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_user_of_accessible_pages(self):
        """Проверка доступности адреса."""
        available_pages = {
            '/auth/signup/': 'users/signup.html',
            '/auth/logout/': 'users/logged_out.html',
            '/auth/login/': 'users/login.html',
            #  'auth/password_reset/': 'users/password_reset_form.html',
            #  'auth/password_reset/done/': 'users/password_reset_done.html',
            #  'auth/reset/<uidb64>/<token>/': 'users/password_reset_confirm.html',
            '/auth/reset/done/': 'users/password_reset_complete.html',
            #  '/auth/password_change/': 'users/password_change_form.html',
            #  '/auth/password_change/done/': 'users/password_change_done.html',
        }
        for address, template in available_pages.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(
                    response,
                    template,
                    'Метод test_user_of_accessible_pages работает неправильно'
                )