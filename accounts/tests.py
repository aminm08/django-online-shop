from django.test import TestCase
from django.urls import reverse

class LoginTest(TestCase):
    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code,200)
    def test_login_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)
    def test_login_content(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response,'Login')
    def test_login_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response,'registration/login.html')

class SignUpTest(TestCase):
    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200)
    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
    def test_signup_content(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response,'Sign up')
    def test_signup_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response,'registration/signup.html')

class SignUpEditTest(TestCase):
    def test_sign_up_edit_url(self):
        response = self.client.get('/accounts/signupchange/')
        self.assertEqual(response.status_code,200)
    def test_sign_up_edit_url_by_name(self):
        response = self.client.get(reverse('edit_signup'))
        self.assertEqual(response.status_code,200)
    def test_sign_up_edit_content(self):
        response = self.client.get(reverse('edit_signup'))
        self.assertContains(response,'Edit sign up')
    def test_sign_up_edit_template_used(self):
        response = self.client.get(reverse('edit_signup'))
        self.assertTemplateUsed(response,'registration/edit.html')

