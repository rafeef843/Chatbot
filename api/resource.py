# api/resources.py
from tastypie.resources import ModelResource
from api.models import Note
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 


class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        
@api_view(['POST'])
def post_element(request):
  
    if request.method == 'POST':
     
        return Response({"message" : "DONE"})