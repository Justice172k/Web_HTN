from dataclasses import field
from operator import imod
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from polls.models import InforSensor, ControlBoard


class InforSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InforSensor
        fields = ['nhiet_do', 'do_am', 'anh_sang']


class ControlBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlBoard
        fields = ['hex', 'r', 'g', 'b', 'Pump', 'Brightness']
