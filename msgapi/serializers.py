from rest_framework import serializers
from msgapi.models import Msgapi, Pvapi

class MsgapiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Msgapi
    fields = '__all__'

class PvapiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pvapi
    fields = '__all__'