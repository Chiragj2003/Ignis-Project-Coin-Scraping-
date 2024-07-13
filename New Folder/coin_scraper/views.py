from django.http import JsonResponse

def start_scraping(request):
    if request.method == 'POST':
        # Your logic to start scraping job here
        return JsonResponse({'status': 'success', 'message': 'Scraping job started successfully.'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
