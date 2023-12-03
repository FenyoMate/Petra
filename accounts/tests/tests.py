import coverage
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.forms import SignUpForm, SetupForm, LoginForm
from accounts.models import Worker, Role, superContext
from accounts.views import login, signup


# Create your tests here.

cov = coverage.coverage()
cov.start()

# Site tests

class LoginTests(TestCase):
    def setUp(self):
        url = reverse('login')
        data = {
            'username': 'john',
            'password': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('profile')

    def test_redirection(self):
        self.assertRedirects(self.response, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_isAuth(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)
    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, LoginForm)

    def form_inputs(self):
        self.assertContains(self.response, '<input', 2)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="password"', 1)

    def test_login_success(self):
        url = reverse('setup')
        data = {
            'name': 'Teszt',
            'password': 'abcdef123456',
        }
        self.response = self.client.post(url, data)
        self.home_url = resolve('/profile/')
        self.assertRedirects(self.response, self.home_url)


def test_login_view_status_code(self):
    url = reverse('login')
    response = self.client.get(url)
    self.assertEquals(response.status_code, 200)


def test_login_url_resolves_view(self):
    view = resolve('/')
    self.assertEquals(view.func, login)


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        '''
        The view must contain five inputs: csrf, username, email, password1, password2
        '''
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456',
            'accept': True
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('setup')

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have an `user` to its context, after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


def test_setup_success():
    url = reverse('setup')


class SetupTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'name': 'John',
            'firstname': 'Doe',
            'lastname': 'John',
            'title': Role.objects.create(name='Admin'),
            'desk': '1'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('profile')

    def test_Admin_creation(self):
        self.assertTrue(Role.objects.exists())

    def test_setup_status(self):
        url = reverse('setup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)



class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2', 'accept']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

cov.stop()
cov.save()
cov.html_report()