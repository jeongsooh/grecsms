from rest_framework import serializers
from msgapi.models import Msgapi

class MsgapiSerializer(serializers.ModelSerializer):
  # msg_content = serializers.JSONField()
  class Meta:
    model = Msgapi
    fields = '__all__'