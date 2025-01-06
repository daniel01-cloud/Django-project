from django.db import models

# Create your models here.

class Quotes(models.Model):
    quote_text = models.TextField()  # The quote text
    author_name = models.CharField(max_length=255)
    image_url = models.URLField()  # URL of the image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name}"
    
    class Meta:
        verbose_name_plural = 'Quotes'