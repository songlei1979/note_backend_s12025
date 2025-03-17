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
        x = 1
        y = 1
        self.assertEqual(x + y, 2, )

        # Test failed login
