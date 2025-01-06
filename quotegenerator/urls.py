from django.urls import path
from .views import random_quotes

app_name = 'quotegenerator'

urlpatterns = [
    path('random_quotes/', random_quotes, name='random-quote'),  # Correct name for the view
]
