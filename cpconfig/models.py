from django.db import models
# from evuser.models import Evuser
# from evcharger.models import Evcharger

# Create your models here.

class Cpconfig(models.Model):
  cpnumber = models.CharField(max_length=128, verbose_name='충전기번호')
  cpserial = models.CharField(max_length=128, verbose_name='시리얼넘버')

  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

  class Meta:
    db_table = 'ocpp_svr_cpconfig'
    ordering = ['register_dttm']
    verbose_name = '충전기설정'
    verbose_name_plural = '충전기설정'
