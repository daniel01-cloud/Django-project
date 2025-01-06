import requests
from django.shortcuts import render
from .models import Quotes
from django.contrib.auth.decorators import login_required

@login_required

def random_quotes(request):
    # API endpoints for random quotes and images
    quote_api_url = 'https://zenquotes.io/api/random'
    picsum_api_url = 'https://picsum.photos/800/600'
    
    # Make requests to the APIs
    quote_response = requests.get(quote_api_url)
    picsum_response = requests.get(picsum_api_url)
    
    # Set default values for quote and image
    quote = "No quote available"
    author = "Unknown"
    image_url = None 
    
    # Check if both responses are successful
    if quote_response.status_code == 200 and picsum_response.status_code == 200:
        quote_data = quote_response.json()
        image_url = picsum_response.url
        if isinstance(quote_data, list) and len(quote_data) > 0:
            quote = quote_data[0].get('q', "No quote available")
            author = quote_data[0].get('a', "Unknown")
    
    # Save the quote and image to the database
    Quotes.objects.create(quote_text=quote, author_name=author, image_url=image_url)
    
    # Prepare context for rendering
    context = {
        'quote': quote,
        'author': author,
        'image_url': image_url,
    }
    
    # Render the template with context
    return render(request, 'quotegenerator/random_quotes.html', context)
