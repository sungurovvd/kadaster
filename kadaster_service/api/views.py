from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RequestHistory
from .serializers import RequestHistorySerializer
from django.http import JsonResponse, HttpResponse
import requests
from requests.exceptions import Timeout
import random

@api_view(['POST'])
def query(request):
    cadastre_number = request.data.get('cadastre_number')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')

    """ так бы примерно выглядела отправка запроса
    external_server_url = 'https://example.com/'
    answer = None
    params = {'cadastre_number': cadastre_number, 'latitude': latitude, 'longitude': longitude}

    try:
        response = requests.get(external_server_url, params=params, timeout=60)

        if response.status_code == 200:
            if response.text.lower() == 'true':
                answer = True
            elif response.text.lower() == 'false':
                answer = False
            else:
                answer = 'strange answer'
        else:
            answer = 'error'
    except Timeout:
        answer = 'timeout'
    except Exception as e:
        answer = str(e)
    """

    external_response = random.choice([True, False])
    request_history = RequestHistory.objects.create(
        cadastre_number=cadastre_number,
        latitude=latitude,
        longitude=longitude,
        response=external_response
    )
    return Response({'result': external_response}, status=status.HTTP_200_OK)

@api_view(['POST'])
def result(request):
    cadastre_number = request.data.get('cadastre_number')
    request_history = RequestHistory.objects.get(cadastre_number=cadastre_number)
    serializer = RequestHistorySerializer(request_history)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def history(request):
    history = RequestHistory.objects.all()
    serializer = RequestHistorySerializer(history, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ping(request):
    return JsonResponse({'status': 'Server is running'}, status=200)
