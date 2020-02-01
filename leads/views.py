from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def test_view(request):
    data = {
        'name' : 'sandeep',
        'age': 18
    }
    return JsonResponse(data)