# @author Chris Atkinson, Conor Martin

import requests
import json
import urllib.parse
import http.client
import time
import RPi.GPIO as GPIO
import time
import random

# Lab2Part3
key = "LQ1LYNA564IB0EX5"  # Server RPi write key
channel = 21  # This number corresponds to the GPIO channel that we have assigned to the sensor
GPIO.setmode(GPIO.BCM)  # Setup GPIO I/O naming scheme to BCM
GPIO.setup(channel, GPIO.IN)  # Sets GPIO 21 to an input pin


# This function sets up the connection between the RPi and the thing speak channel
def readServerRPi():
    URL = 'https://api.thingspeak.com/channels/1155565/feeds.json?api_key=8JDWE6GONX7QWNAR&results=2'  # Headless RPi thing speak channel
    KEY = '8JDWE6GONX7QWNAR'  # Headless RPi read key
    HEADER = '&results=2'
    NEW_URL = URL + KEY + HEADER
    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_1 = get_data['feeds']
    return (field_1)[0]


# This function reads the data from the moisture sensor returning 1 on a high
# moisture level and 0 on a low moisture level
def getMoisture(channel):
    if GPIO.input(channel):
        print("no water detected")  # prints no water detected if there is no moisture in the soil
        return 0
    else:
        print("water detected")  # prints water detected if there is moisture in the soil
        return 1


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  #
GPIO.add_event_callback(channel, getMoisture)  #


# We used a random number generator to simulate the output of a pH sensor
# since we could not afford to buy one of our own
def getpH():
    return random.randint(60, 80) / 10


# This is the function that sends the data collected to the thing speak server
def transmission():
    while True:
        moisture = getMoisture(channel)  # Sets the data to be sent
        pH = getpH()
        params = urllib.parse.urlencode({'field1': moisture, 'field2': pH, 'key': key})
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


# This while loop waits for the server to send a request for information
# if the id associated with that request is the same as the id for theis RPi
# then the data is transmitted
while True:
    currentID = readServerRPi()['entry_id']
    field = readServerRPi()

    if field['entry_id'] > (currentID):
        currentID = field['entry_id']
        if field['field1'] == '5':  # Checks if the server RPi is sending a request to this RPi
            transmission()
            print(field['field2'])

