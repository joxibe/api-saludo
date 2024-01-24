from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def saludo(request, nombre):
    if request.method == 'GET':
        data = f'Hola {nombre}'
        return JsonResponse({'mensaje': data})
