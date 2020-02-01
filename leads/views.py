from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name' : 'sandeep',
            'age': 18
        }
        return Response(data)


# def test_view(request):
#     data = {
#         'name' : 'sandeep',
#         'age': 18
#     }
#     return JsonResponse(data)