import json
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from quotegenerator.models import Quotes

class RandomQuotesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('quotegenerator:random-quote')

    @patch('quotegenerator.views.requests.get')
    def test_random_quotes_view_successful(self, mock_get):
        # Mock API responses
        mock_quote_response = [
            {"q": "Test Quote", "a": "Test Author"}
        ]
        mock_image_response = "https://picsum.photos/800/600"
        
        mock_get.side_effect = [
            # First call to quote API
            type('MockResponse', (object,), {"json": lambda: mock_quote_response, "status_code": 200}),
            # Second call to image API
            type('MockResponse', (object,), {"url": mock_image_response, "status_code": 200})
        ]

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'qoutegenerator/random_quotes.html')
        self.assertContains(response, "Test Quote")
        self.assertContains(response, "Test Author")

    def test_random_quotes_view_database_entry(self):
        # Check if the view creates a new entry in the database
        Quotes.objects.create(quote_text="Test Quote", author_name="Test Author", image_url="https://example.com")
        self.assertEqual(Quotes.objects.count(), 1)
