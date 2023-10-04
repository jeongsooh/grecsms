from django import forms
from clients.models import Clients

class ClientsResetForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  reset_type = forms.CharField(
    max_length=8, required=False, label='리셋타입'
  )
  connector_id = forms.CharField(
    max_length=64, required=False, label='커넥터아이디'
  )
  msg_content = forms.CharField(
    max_length=512, required=False, label='기타메세지묶음'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class RemoteStartForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  id_tag = forms.CharField(
    max_length=64, initial="0000000000150049", label='아이디태그'
  )
  charging_profile = forms.CharField(
    max_length=512, required=False, label='충전프로파일'
  )


  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ChargingProfileForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터번호')
  charging_profile_purpose = forms.CharField(max_length=64, label='충전프로파일퍼포스')
  charging_profile_kind = forms.CharField(max_length=64, label='충전프로파일카인드')
  duration = forms.IntegerField(label='프로파일지속시간')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class CompositeScheduleForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터번호')
  duration = forms.IntegerField(label='프로파일지속시간')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

class ClearChargingProfileForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  connector_id = forms.IntegerField(label='커넥터번호')
  profile_id = forms.IntegerField(label='프로파일아이디')

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        clients = Clients.objects.get(cpnumber=cpnumber)
      except Clients.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = clients.id

