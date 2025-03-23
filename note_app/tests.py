# test_auth.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        self.user = User.objects.create_user(**self.credentials)
        self.token_url = reverse('login')

    def test_token_login(self):
        # Simulate login to get token
        response = self.client.post(self.token_url, self.credentials)

        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the token is in the response
        self.assertIn('token', response.data)

        # Use the token to authenticate further requests
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)