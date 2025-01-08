from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
import io

class UploadCSVViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/upload-csv/'

    def test_upload_valid_csv(self):
        file_data = io.StringIO("name,email,age\nJohn Doe,john@example.com,30\nJane Doe,jane@example.com,25")
        response = self.client.post(self.url, {'file': file_data}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)

    def test_upload_invalid_csv(self):
        file_data = io.StringIO("name,email,age\nJohn Doe,john@example,30\nJane Doe,jane@example.com,130")
        response = self.client.post(self.url, {'file': file_data}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(len(response.data['errors']), 2)
