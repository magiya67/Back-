from django.shortcuts import render
from django.http import JsonResponse
import requests
def second_serv_request(request):
    try:
        url = "http://127.0.0.1:8000/"
        response = requests.get(url)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.RequestException as e:
        return JsonResponse({"error": "Не получилось, связи нет", "details": str(e)}, status=500)
# Create your views here.
