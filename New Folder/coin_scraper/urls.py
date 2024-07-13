# coin_scraper/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('start_scraping/', views.start_scraping, name='start_scraping'),
]
