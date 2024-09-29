from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, UploadedFile
from rest_framework.authtoken.models import Token

class UserAPITests(APITestCase):

    def setUp(self):
        self.client_user = User.objects.create_user(
            username='testclient',
            password='testpass',
            role='client'
        )
        self.ops_user = User.objects.create_user(
            username='testops',
            password='testpass',
            role='ops'
        )
        self.token = Token.objects.create(user=self.client_user)
        self.ops_token = Token.objects.create(user=self.ops_user)

    def test_signup_client_user(self):
        url = reverse('signup')
        data = {
            'username': 'rishabho',
            'password': 'yes',
            'role': 'client'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)

    def test_login_user(self):
        url = reverse('login')
        data = {
            'username': 'testclient',
            'password': 'testpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_upload_file_as_ops_user(self):
        url = reverse('upload-file')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.ops_token))
        with open('testfile.doc', 'w') as f:
            f.write("This is a test file.")
        with open('testfile.doc', 'rb') as f:
            response = self.client.post(url, {'file': f}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)

    def test_upload_file_as_client_user(self):
        url = reverse('upload-file')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        with open('testfile.txt', 'w') as f:
            f.write("This is a test file.")
        with open('testfile.txt', 'rb') as f:
            response = self.client.post(url, {'file': f}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('error', response.data)

    def test_list_files_as_client_user(self):
        url = reverse('list-files')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('files', response.data)

    def test_download_file_as_client_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.ops_token))
        with open('testfile.txt', 'w') as f:
            f.write("This is a test file.")
        with open('testfile.txt', 'rb') as f:
            self.client.post(reverse('upload-file'), {'file': f}, format='multipart')

        url = reverse('download-file', kwargs={'file_id': 1})  
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('download-link', response.data)

    def tearDown(self):
        User.objects.all().delete()
        UploadedFile.objects.all().delete()
