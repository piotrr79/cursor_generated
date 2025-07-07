from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from typing import Any

# Create your tests here.

class UserAuthTests(APITestCase):
    """
    Unit tests for user registration and login endpoints.
    """
    def test_register(self) -> None:
        url = reverse('register')
        data = {'email': 'test@example.com', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login(self) -> None:
        # Register first
        self.client.post(reverse('register'), {'email': 'test2@example.com', 'password': 'testpass123'})
        url = reverse('login')
        data = {'email': 'test2@example.com', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid(self) -> None:
        url = reverse('login')
        data = {'email': 'notfound@example.com', 'password': 'wrongpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
