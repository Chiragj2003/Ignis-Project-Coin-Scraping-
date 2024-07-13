from celery import shared_task
from .coinmarketcap import CoinMarketCap
from .models import  Task

from celery import shared_task
from .coinmarketcap import CoinMarketCap

@shared_task
def start_scraping(job_id, coins):
    coinmarketcap = CoinMarketCap()
    for coin in coins:
        data = coinmarketcap.scrape_data(coin)
        # Save the data to the database
        Task.objects.create(job_id=job_id, coin=coin, output=data)
    coinmarketcap.close()