from ast import If
import paho.mqtt.client as mqtt
import sqlite3
import json


def get_client():
    def on_connect(client, userdata, flags, rc):
        print("success")
    client = mqtt.Client()
    client.connect('broker.emqx.io', 1883, 60)
    client.on_connect = on_connect
    return client


def subcribe(client: mqtt.Client):
    def on_message(client, userdata, msg):
        from .models import InforSensor
        pay = json.loads(msg.payload.decode("utf-8"))
        InforSensor(
            nhiet_do=pay["nhiet_do"], do_am=pay["do_am"], anh_sang=pay["anh_sang"]).save()

    client.on_message = on_message
    client.subscribe('esp8266/message')


def publish(client: mqtt.Client, tmp):
    client.publish('esp8266/message', payload=tmp, qos=0)
