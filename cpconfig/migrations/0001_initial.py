# Generated by Django 4.1.5 on 2023-08-25 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpconfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpnumber', models.CharField(max_length=128, verbose_name='충전기번호')),
                ('cpserial', models.CharField(max_length=128, verbose_name='시리얼넘버')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록일시')),
            ],
            options={
                'verbose_name': '충전기설정',
                'verbose_name_plural': '충전기설정',
                'db_table': 'ocpp_svr_cpconfig',
            },
        ),
    ]
