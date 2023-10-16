# Generated by Django 4.1.5 on 2023-10-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variables', '0002_alter_variables_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confkeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=64, verbose_name='키네임')),
                ('readonly', models.CharField(blank=True, max_length=64, verbose_name='권한설정')),
                ('value', models.CharField(blank=True, max_length=64, verbose_name='설정값')),
            ],
            options={
                'verbose_name': '설정값',
                'verbose_name_plural': '설정값',
                'db_table': 'ocpp_svr_confkeys',
            },
        ),
        migrations.AlterField(
            model_name='variables',
            name='interval',
            field=models.IntegerField(null=True, verbose_name='설정값'),
        ),
    ]
