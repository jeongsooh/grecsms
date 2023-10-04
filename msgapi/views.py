from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MsgapiSerializer

from msgapi.models import Msgapi

import json

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List':'/msgapi-list/',
    'Detail View':'/msgapi-detail/<str:pk>/',
    'Create':'/msgapi-create/',
    'Update':'/msgapi-update/<str:pk>/',
    'Delete':'/msgapi-delete/<str:pk>/',
    }

  return Response(api_urls)

@api_view(['GET'])
def msgapiList(request):
  msgapis = Msgapi.objects.all()
  serializer = MsgapiSerializer(msgapis, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def msgapiDetail(request, pk):
  msgapis = Msgapi.objects.get(id=pk)
  serializer = MsgapiSerializer(msgapis, many=False)

  return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def msgapiCreate(request):

  try:
    data = json.loads(request.body)
  except:
    return Response({"message":"ERROR DETECT"})

  serializer = MsgapiSerializer(data=data)
  # print(serializer)
  if serializer.is_valid():
    serializer.save()
    print("serializer is valid")
  else:
    print("serializer is NOT valid")
    # print(serializer.errors)

  return Response(serializer.data)

@api_view(['POST'])
def msgapiUpdate(request, pk):
  msgapi = Msgapi.objects.get(id=pk)
  serializer = MsgapiSerializer(instance=msgapi, data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def msgapiDelete(request, pk):
  msgapi = Msgapi.objects.get(id=pk)
  msgapi.delete()

  return Response("Item is successfully deleted!")

class MsgapiList(ListView):
  model = Msgapi
  template_name='msgapi.html'
  context_object_name = 'msgapiList'
  paginate_by = 10
  queryset = Msgapi.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['apiinuser'] = user_id
    return context
