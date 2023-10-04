from django import forms
from evcharger.models import Evcharger

class EvchargerResetForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')

    if cpnumber:
      try:
        evcharger = Evcharger.objects.get(cpnumber=cpnumber)
      except Evcharger.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.cpnumber = evcharger.id

class EvchargerRegisterForm(forms.Form):
  cpnumber = forms.CharField()
  cpsite = forms.CharField()
  partner_id = forms.CharField()
  manager_id = forms.CharField()
  public_use = forms.CharField()
  cpstatus = forms.CharField()
  address = forms.Textarea()
  cpmodel = forms.CharField()
  cpmaker = forms.CharField()
  fwversion = forms.CharField()