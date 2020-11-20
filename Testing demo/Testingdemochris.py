import requests
import json
import urllib.parse
import http.client
import time
import RPi.GPIO as GPIO
import time
import random

# Lab2Part3
key = "LQ1LYNA564IB0EX5"
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def readServerRPi():
    URL = 'https://api.thingspeak.com/channels/1155565/feeds.json?api_key=8JDWE6GONX7QWNAR&results=2'
    KEY = '8JDWE6GONX7QWNAR'
    HEADER = '&results=2'
    NEW_URL = URL + KEY + HEADER
    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_1 = get_data['feeds']
    return (field_1)[0]

def getMoisture(channel):
    if GPIO.input(channel):
        print("no water detected")
        i = 0
    else:
        print("water detected")
        i = 1
    return i
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, getMoisture)

def getpH():
    return random.randint(60,80)/10

def transmission():
    while True:
        moisture = getMoisture(channel)
        pH = getpH()
        params = urllib.parse.urlencode({'field1': moisture,'field2': pH, 'key': key})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(moisture)
            print(pH)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break




while True:
    currentID = readServerRPi()['entry_id']
    field = readServerRPi()

    if field['entry_id'] > (currentID):
        currentID = field['entry_id']
        if field['field1'] == '5':
            transmission()
            print(field['field2'])

