from django.shortcuts import render
from django.http import JsonResponse


def home_api(request):
    data = {
        "name": "henry",
        "adress": "clarusway.com",
        "skills": ["python", "django"]
    }
    return JsonResponse(data)
