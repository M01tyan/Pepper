# coding=utf8

from time import sleep
import paho.mqtt.client as mqtt

host = '172.21.14.129'#home 192.168.100.104 #U-Aizu 172.21.14.129
port = 1883
topic = 'PEPPER/pepper_1/cmd'

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.connect(host, port=port, keepalive=60)

client.publish(topic, 'hello world')
sleep(0.2)

client.disconnect()
