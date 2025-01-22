from django.shortcuts import render
from django.http import JsonResponse

def another_serv_request(request):
    return JsonResponse({'message': "HELLO MOTO (server 1)"})


# Create your views here.
