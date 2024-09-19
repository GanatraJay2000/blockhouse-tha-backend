# tests.py in your Django app
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ChartAPITests(APITestCase):
    def test_candlestick_data(self):
        url = reverse('candlestick_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_line_chart_data(self):
        url = reverse('line_chart_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_bar_chart_data(self):
        url = reverse('bar_chart_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_pie_chart_data(self):
        url = reverse('pie_chart_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_all_data(self):
        url = reverse('all_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
