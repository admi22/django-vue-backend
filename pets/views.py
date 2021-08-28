from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.middleware.csrf import get_token
from .models import Pet

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})
