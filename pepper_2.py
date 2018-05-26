# coding=utf8
import paho.mqtt.client as mqtt
import requests as https
import random
from time import sleep
from inputimeout import inputimeout, TimeoutOccurred
#MQTT base Infomation
host = '192.168.100.104'#home 192.168.100.104 #U-Aizu 172.21.14.129
port = 1883
topic = 'PEPPER/pepper_2/'

#connet MQTT
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.connect(host, port=port, keepalive=60)

def checkFace():
    print("こんにちは。お客様の目的地を検索しますので、私の前に来ていただけませんか？")
    face = takePictureFace()
    print("お顔を認証いたしました。目的地を検索しておりますので、10秒程度お待ちいただけますか")
    client.publish(topic+'attrs', 'face|'+face)
    client.publish(topic+'cmdexe', 'facedetect|success')

def takePictureFace():
    num = random.randint(1,10)
    if(num > 6):
        return 'face.jpg'
    else:
        print("申し訳ありませんが、もう一度お顔の写真を撮らせてください")
        tackPictureFace()

def guidStartPepper2():
    print("誘導ロボットが参ります。もうしばらくお待ち下さい")
    client.publish(topic+'cmdexe', 'handover|success')

def reAsk():
    list = getDestinationList()
    print("申し訳ありませんが、もう一度目的地を教えてください")
    for i in list:
        print(i)
    while True:
        try:
            goal = inputimeout(prompt='>>', timeout=5)
            break
        except TimeoutOccurred:
            print("申し訳ありませんが、目的地を教えてください")
    client.publish(topic+'attrs', 'dest|'+goal)
    client.publish(topic+'cmdexe', 'reask|success')

def getDestinationList():
    list = ("会議室4", "会議室5")
    return list
