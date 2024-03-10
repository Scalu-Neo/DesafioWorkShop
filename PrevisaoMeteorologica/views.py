import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_local_clima(request, cidade):
    chaveApi = '984adb41f0349ae6ebf5602d61c1b5f3'
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chaveApi}')
    data = response.json()
    return JsonResponse(data)

