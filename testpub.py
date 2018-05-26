# coding=utf8

import paho.mqtt.client as paho

mqttc = paho.Client(protocol=mqtt.MQTTv311)

mqttc.connect("192.168.100.104", 1883, 60)
mqttc.publish("PEPPER/pepper_1/cmd", "hello world", 1)
