from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_url(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code,200)
    def test_home_page_url_by_name(self):
        result = self.client.get(reverse('homepage'))
        self.assertEqual(result.status_code,200)
    def test_home_page_content(self):
        result = self.client.get(reverse('homepage'))
        self.assertContains(result,'home page')
    def test_home_page_template_uesd(self):
        result = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(result,'home_page.html')


class AboutUsPageTest(TestCase):
    def test_about_us_url(self):
        response = self.client.get('/about us/')
        self.assertEqual(response.status_code,200)
    def test_about_us_page_url_by_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code,200)
    def test_about_us_page_content(self):
        response = self.client.get(reverse('about_us'))
        self.assertContains(response,'about us')
    def test_about_us_page_template_used(self):
        response = self.client.get(reverse('about_us'))
        self.assertTemplateUsed(response,'about_us.html')

