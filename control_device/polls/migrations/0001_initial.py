# Generated by Django 4.0.3 on 2022-03-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusLedRed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_led', models.CharField(max_length=20)),
                ('time_public', models.DateTimeField()),
            ],
        ),
    ]
