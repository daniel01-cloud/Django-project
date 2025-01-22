import requests
from django.shortcuts import render

def top_headlines(request):
    api_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=23589164fef64ea48c70d4a35056afb9"
    response = requests.get(api_url)
    
    
    
    # Extract articles and log them
    articles = response.json().get('articles', [])
    
    return render(request, 'news/top_headlines.html', {'articles': articles})
