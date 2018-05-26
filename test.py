#coding: utf-8
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 51975)#pepper port 9559

tts.say("こんにちは")
