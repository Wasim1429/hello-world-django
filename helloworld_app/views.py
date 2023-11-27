from django.shortcuts import render
from django.http import JsonResponse


def template_view(request):
    return render(request, 'home.html', {'message': 'Hello World!'})


def json_view(request):
    return JsonResponse({"Message": "Hello World!"})
