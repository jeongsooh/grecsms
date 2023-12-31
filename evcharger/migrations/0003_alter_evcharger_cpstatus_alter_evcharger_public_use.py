# Generated by Django 4.2.4 on 2023-08-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evcharger', '0002_alter_evcharger_cpstatus_alter_evcharger_public_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evcharger',
            name='cpstatus',
            field=models.CharField(choices=[('정상', '공용'), ('정지', '비공용'), ('가동대기', '가동대기')], default='정상', max_length=64),
        ),
        migrations.AlterField(
            model_name='evcharger',
            name='public_use',
            field=models.CharField(choices=[('공용', '공용'), ('비공용', '비공용')], default='공용', max_length=64),
        ),
    ]
