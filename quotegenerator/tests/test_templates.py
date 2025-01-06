from django.test import TestCase, Client
from django.urls import reverse
from quotegenerator.models import Quotes

class RandomQuotesTemplateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('quotegenerator:random-quote')
        Quotes.objects.create(
            quote_text="Test Quote",
            author_name="Test Author",
            image_url="https://example.com/image.jpg"
        )

    def test_random_quotes_template_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Test Quote")
        self.assertContains(response, "Test Author")
        self.assertContains(response, "https://example.com/image.jpg")
