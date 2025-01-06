from django.test import TestCase
from quotegenerator.models import Quotes

class QuotesModelTest(TestCase):
    def test_create_quote(self):
        quote = Quotes.objects.create(
            quote_text="Life is beautiful",
            author_name="Author Test",
            image_url="https://example.com/image.jpg"
        )
        self.assertEqual(str(quote), "Life is beautiful - Author Test")
        self.assertEqual(Quotes.objects.count(), 1)
