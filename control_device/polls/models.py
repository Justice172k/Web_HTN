from django.db import models

# Create your models here.


class InforSensor(models.Model):
    nhiet_do = models.IntegerField()
    do_am = models.IntegerField()
    anh_sang = models.IntegerField()
    # time_publish = models.DateTimeField()


class ControlBoard(models.Model):
    hex = models.CharField(max_length=20)
    r = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    b = models.IntegerField(default=0)
    Pump = models.CharField(max_length=20)
    Brightness = models.IntegerField()
