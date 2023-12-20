from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MsgapiSerializer, PvapiSerializer

from msgapi.models import Msgapi, Pvapi

import json
import random
import string
from datetime import datetime


def password_gen():
  len_alphabet = 10
  len_digit = 10
  len_special = 4

  letters = list()

  for l in range(len_alphabet):
      letters.append(random.choice(list(set(string.ascii_letters) - set('lIO'))))

  for d in range(len_digit):
      letters.append(random.choice(list(set(string.digits) - set('01'))))

  for s in range(len_special):
      letters.append(random.choice('!@#$%^&*?'))

  random.shuffle(letters)
  return ''.join(letters)







# Create your views here.

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    # 'List':'/msgapi-list/',
    'List2':'/pvapi-list/',
    # 'Detail View':'/msgapi-detail/<str:pk>/',
    'Detail2 View':'/pvapi-detail/<str:pk>/',
    # 'Create':'/msgapi-create/',
    'Create':'/pvapi-create/',
    'Create2':'/pvapi-create2',
    'Update':'/msgapi-update/<str:pk>/',
    # 'Delete':'/msgapi-delete/<str:pk>/',
    'Delete2':'/pvapi-delete/<str:pk>/',
    }

  return Response(api_urls)

@api_view(['GET'])
def msgapiList(request):
  msgapis = Msgapi.objects.all()
  serializer = MsgapiSerializer(msgapis, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def pvapiList(request):
  msgapis = Pvapi.objects.all()
  serializer = PvapiSerializer(msgapis, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def msgapiDetail(request, pk):
  msgapis = Msgapi.objects.get(id=pk)
  serializer = MsgapiSerializer(msgapis, many=False)

  return Response(serializer.data)

@api_view(['GET'])
def pvapiDetail(request, pk):
  msgapis = Pvapi.objects.get(id=pk)
  serializer = PvapiSerializer(msgapis, many=False)

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

@csrf_exempt
@api_view(['POST'])
def pvapiCreate(request):
  print("================================================")
  print(request.body)
  print("================================================")
  try:
    data = json.loads(request.body)
  except:
    return Response({"message":"ERROR DETECT"})
  
  id = data['origin'][5:].strip()
  data_return = {
    'origin': data['origin'],
    'client_id': "PL10" + id,
    'pwd': password_gen()
  }

  serializer = PvapiSerializer(data=data_return)
  if serializer.is_valid():
    serializer.save()
    print("serializer is valid")
  else:
    print("serializer is NOT valid")
    # print(serializer.errors)

  data_echo = {
    'code': 200,
    'status': 'OK',
    'message': 'Success',
    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'data': {
      'clientId': serializer.data['client_id'],
      'pwd': serializer.data['pwd']
    }
  }
  return Response(data_echo)

@csrf_exempt
@api_view(['POST'])
def pv2apiCreate(request):
  try:
    origin = request.GET.get('origin')
  except:
    return Response({"message":"ERROR DETECT"})
  
  id = origin[5:].strip()
  data_return = {
    'origin': origin,
    'client_id': "PL10" + id,
    'pwd': password_gen()
  }

  serializer = PvapiSerializer(data=data_return)
  if serializer.is_valid():
    serializer.save()
    print("serializer is valid")
  else:
    print("serializer is NOT valid")
    # print(serializer.errors)

  data_echo = {
    'code': 200,
    'status': 'OK',
    'message': 'Success',
    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'data': {
      'clientId': serializer.data['client_id'],
      'pwd': serializer.data['pwd']
    }
  }
  return Response(data_echo)

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

@api_view(['DELETE'])
def pvapiDelete(request, pk):
  msgapi = Pvapi.objects.get(id=pk)
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
