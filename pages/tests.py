from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
# Create your tests here.

class TestPages(TestCase):
    username = 'ali'
    email = 'ali@ali.com'

    def test_home_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Here is Home')

    def test_home_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)    

    def test_login_by_url(self):
        response = self.client.get(reverse('login')) 
        self.assertEqual(response.status_code, 200)    

    def test_signup_by_url(self):
        response = self.client.get(reverse('signup')) 
        self.assertEqual(response.status_code, 200)        

    def test_signup_form(self):
        
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
            )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
