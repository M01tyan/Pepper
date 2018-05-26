# coding=utf8
import paho.mqtt.client as mqtt
import random
from time import sleep
from naoqi import ALProxy
#from table import *
#MQTT base Infomation
host = '192.168.100.104'#home 192.168.100.104 #U-Aizu 172.21.14.129
port = 1883
topic = 'PEPPER/pepper_1/#'
tts = ALProxy("ALTextToSpeech", "localhost", 51172)
m = ALProxy("ALMotion", "localhost", 51172)

def showDestinationList():
    #フロア情報を取得
    list = getDestinationList()
    #右手を挙げてお辞儀する
    bowPepper()
    tts.say("受付担当のPEPPER(一階受付前)です。よろしくお願いします。")
    tts.say("目的地を教えてください")
    #タブレット上にフロアマップを表示
    #viewTable()

    #client.publish(topic+'attrs', 'face|'+face+'|dest|'+goal)
    #client.publish(topic+'cmdexe', 'welcome|success')

def getDestinationList():
    list = (("1階", "2階", "3階"),
            ("会議室1", "会議室2", "会議室3", "会議室4"),
            ("会議室5", "会議室6", "会議室7"),
            ("サイバールーム"))
    return list

def bowPepper():
    m.changeAngles("HeadYaw", 0.25, 0.05)

def checkGoal(goal):
    tts.say("会議室"+goal+"ですね。" ,)
    if goal < '4':
        tts.say("確認いたしますので少しお待ち下さい。")
    elif goal < '6':
        tts.say("案内する時に必要になるため、申し訳ありませんが、お顔の写真を撮らせてください。")
        face = takePictureFace(goal)
    else:
        tts.say("入館証がお手元にあることをご確認ください。")

def takePictureFace(goal):
    num = random.randint(1,10)
    if(num > 6):
        return 'face.jpg'
    else:
        tts.say("申し訳ありませんが、もう一度お顔の写真を撮らせてください")
        checkGoal(goal)

def guidStartPepper1(payload):
    if '1' in str(payload):
        tts.say("誘導ロボットが参ります。もうしばらくお待ちください")
    elif '2' in str(payload):
        tts.say("誘導ロボットが参ります。エレベーター前まで誘導いたしますので、２階へおあがりください。２階のカメラを覗き込んでいただきますと、２階でまた誘導ロボットが参ります。")
    else:
        tts.say("出迎えの者が参りますので、ここで少しお待ち下さい。")
    refreshTablet()

def refreshTablet():
    client.publish(topic+'cmdexe', 'handover|success')
