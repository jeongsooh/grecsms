# from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Cpconfig


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#       model = User
#       fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#       model = Group
#       fields = ['url', 'name']

class CpconfigSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  cpnumber = serializers.CharField(max_length=128)
  cpserial = serializers.CharField(max_length=128)

  # class Meta:
  #     model = Cpconfig

  def create(self, validated_data):
      """
      Create and return a new `Snippet` instance, given the validated data.
      """
      return Cpconfig.objects.create(**validated_data)

  def update(self, instance, validated_data):
      """
      Update and return an existing `Snippet` instance, given the validated data.
      """
      instance.cpnumber = validated_data.get('cpnumber', instance.cpnumber)
      instance.cpserial = validated_data.get('cpserial', instance.cpserial)
      instance.save()
      return instance