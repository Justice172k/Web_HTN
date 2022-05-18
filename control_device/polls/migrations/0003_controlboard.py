# Generated by Django 4.0.2 on 2022-03-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_inforsensor_remove_statusledred_time_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant', models.CharField(max_length=20)),
                ('Pump', models.CharField(max_length=20)),
                ('Mode', models.CharField(max_length=20)),
                ('brightness', models.IntegerField()),
            ],
        ),
    ]
