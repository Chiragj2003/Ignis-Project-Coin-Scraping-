from django.urls import path
from . import views

urlpatterns = [
    path('api/taskmanager/start_scraping/', views.StartScrapingView.as_view()),
    path('api/taskmanager/scraping_status/<uuid:job_id>/', views.ScrapingStatusView.as_view()),
]