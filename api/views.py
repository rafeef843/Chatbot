from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Note

from urllib import request 
from django.shortcuts import render
from django.db import connection

from django.http import JsonResponse 
from rest_framework.decorators import api_view


@api_view(['GET'])
def test( request): 
    return Response({"result": "test Done" })
