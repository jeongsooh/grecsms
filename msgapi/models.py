from django.db import models

# Create your models here.

class Msgapi(models.Model):
  cpnumber = models.CharField(max_length=128, verbose_name='충전기번호')
  carnumber = models.CharField(max_length=128, verbose_name='차량번호')
  connector_id = models.IntegerField(verbose_name='커넥터아이디')

  def __str__(self):
    return self.carnumber

  class Meta:
    db_table = 'ocpp_svr_msgapi'
    verbose_name = '차량번호'
    verbose_name_plural = '차량번호'