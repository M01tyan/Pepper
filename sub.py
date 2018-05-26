# coding=utf8
#mosquitto_pub -h 172.21.14.129 -p 1883 -t PEPPER/pepper_1/cmd -m 'welcome|start'
import paho.mqtt.client as mqtt
from naoqi import ALProxy
from pepper_1 import *
#from pepper_2 import *

host = '192.168.100.104'#home 192.168.100.104 #u-aizu 172.21.14.129
port = 1883
topic = 'PEPPER/#'

def on_connect(client, userdata, flags, respons_code):
    print('status [0]'.format(respons_code))

    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(str(msg.topic) + ' ' + str(msg.payload))
    #welcomeコマンドを受信すると
    #if 'PEPPER/pepper_1/' in str(msg.topic):
    if 'welcome|start' in str(msg.payload):
        #client.disconnect()
        showDestinationList()
    #    elif 'handover|success' in str(msg.payload):
    #        print("ok")
    #    elif 'handover' in str(msg.payload):
    #        guidStartPepper1(msg.payload)

    #elif 'PEPPER/pepper_2/':
    #    if 'facedetect|start' in str(msg.payload):
    #        checkFace()
    #    elif 'handover|continue' in str(msg.payload):
    #        guidStartPepper2()
    #    elif 'reask|true' in str(msg.payload):
    #        reAsk()

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))


if __name__ == '__main__':
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)

    client.loop_forever()
