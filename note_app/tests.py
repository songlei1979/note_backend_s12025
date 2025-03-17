from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


# Create your tests here.
# test my User login



class LoginAPITestCase(TestCase):
    # def setUp(self):
    #     self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
    #     self.client = APIClient()

    def test_login_api(self):
        # Test successful login
        response = self.client.post('/login/', {'username': 'lei7', 'password': 'Unitec123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

        # Test failed login
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 400)

        # Test missing credentials
        response = self.client.post('/login/', {'username': 'testuser'})
        self.assertEqual(response.status_code, 400)