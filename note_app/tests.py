# tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase
from note_app.models import Note
from note_app.serialzers import NoteSerializer


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




class NoteViewSetTestCase(APITestCase):
    def setUp(self):
        self.note1 = Note.objects.create(title='Note 1', content='This is note 1')
        self.note2 = Note.objects.create(title='Note 2', content='This is note 2')
        self.url = '/api/notes/'

    def test_get_all_notes(self):
        response = self.client.get(self.url)
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_valid_note(self):
        response = self.client.get(f'{self.url}{self.note1.id}/')
        serializer = NoteSerializer(self.note1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_note(self):
        response = self.client.get(f'{self.url}999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_note(self):
        data = {'title': 'New note', 'content': 'This is a new note'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 3)
        self.assertEqual(Note.objects.last().title, 'New note')
        self.assertEqual(Note.objects.last().content, 'This is a new note')

    def test_create_invalid_note(self):
        data = {'content': 'This is a new note'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_note(self):
        data = {'title': 'Updated note', 'content': 'This is an updated note'}
        response = self.client.put(f'{self.url}{self.note1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(id=self.note1.id).title, 'Updated note')
        self.assertEqual(Note.objects.get(id=self.note1.id).content, 'This is an updated note')

    def test_update_invalid_note(self):
        data = {'content': 'This is an updated note'}
        response = self.client.put(f'{self.url}{self.note1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_note(self):
        response = self.client.delete(f'{self.url}{self.note1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 1)

    def test_delete_invalid_note(self):
        response = self.client.delete(f'{self.url}999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)