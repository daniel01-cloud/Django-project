from django.urls import path
from . import views

urlpatterns = [
    path('top-headlines/', views.top_headlines, name='news-top-headlines'),
]
