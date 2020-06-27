import json
import uuid
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
# from .models import Person

# Create your views here.


# def write_server(request):
#     print('request.body: ', request.body)

#     data = json.loads(request.body)
#     data['id'] = uuid.uuid4()
#     Person.objects.create(**data)
#     return JsonResponse({'success': True})


# def read_server(request):
#     name = request.GET['name']
#     data = serializers.serialize('python', Person.objects.filter(name=name))
#     return JsonResponse({'success': True, 'data': data})


def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')
