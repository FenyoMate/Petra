from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from PetraBot.views import profile, new_chat, chat, uc
from accounts.views import login, signup, logout, profileSetup, context


# Create your tests here.

# Site tests

class ProfileSetupTests(TestCase):
    def test_view_status_code(self):
        url = reverse('setup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_url_resolves_view(self):
        view = resolve('/setup/')
        self.assertEquals(view.func, profileSetup)


class context_tests(TestCase):
    def setUp(self):
        url = reverse('context')
        auth = {

        }
    def test_context_view_status_code(self):
        url = resolve('/context/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_url_resolves_view(self):
        view = resolve('/context/')
        self.assertEquals(view.func, context)


class ChatTests(TestCase):
    def test_view_status_code(self):
        url = reverse('new_chat')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_url_resolves_view(self):
        view = resolve('/chat/')
        self.assertEquals(view.func, new_chat)

    def test_chat_view_status_code_success(self):
        url = reverse('chat', args=[1])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_chat_view_status_code_fail(self):
        url = resolve('/chat/950/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_chat_url_resolves_view(self):
        view = resolve('/chat/1/')
        self.assertEquals(view.func, chat)


class signupTests(TestCase):
    def test_signup_view_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)


class logoutTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_home_url_resolves_home_view(self):
        view = resolve('/logout/')
        self.assertEquals(view.func, logout)


class ucTests(TestCase):
    def test_view_status_code(self):
        url = reverse('underconstr')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_home_view(self):
        view = resolve('/uc/')
        self.assertEquals(view.func, uc)
