from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import JobSerializer, TaskSerializer
from .tasks import start_scraping
from .coinmarketcap import CoinMarketCap
from .models import Job, Task

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins')
        if not all(isinstance(coin, str) for coin in coins):
            return Response({'error': 'Invalid input'}, status=400)
        job = Job.objects.create()
        start_scraping.delay(job.id, coins)
        return Response({'job_id': job.id})

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        job = Job.objects.get(id=job_id)
        tasks = Task.objects.filter(job=job)
        serializer = TaskSerializer(tasks, many=True)
        return Response({'job_id': job_id, 'tasks': serializer.data})