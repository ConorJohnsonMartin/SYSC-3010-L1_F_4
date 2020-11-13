import requests
import json
import urllib.parse
import http.client
import time

def transmission(field1 = None, field2= None, field3= None, field4= None, field5= None, field6= None, field7= None, field8= None):
    key = "LQ1LYNA564IB0EX5"
    params = urllib.parse.urlencode({'field1': field1, 'field2': field2, 'field3': field3, 'field4': field4, 'field5': field5, 'field6': field6, 'field7': field7, 'field8': field8, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        conn.close()
    except:
        print("connection failed")

def readHeadlessPi():
    url = 'https://api.thingspeak.com/channels/1160322/feeds.json?api_key=HTDCLD7F8EWCLS4L&results=2'
    key = 'HTDCLD7F8EWCLS4L'
    header = '&results=1'

    finalURL = url + key + header

    get_data = requests.get(finalURL).json()

    channel1read = get_data['feeds'][0]

    return channel1read

currentID = readHeadlessPi()['entry_id']

transmission(2, 'test')

broken = 0
while(True):
    broken +=1
    if broken == 20:
        break
    if readHeadlessPi()['entry_id'] == (currentID+1):
        break
    time.sleep(0.1)

print(readHeadlessPi()['field1'])
time.sleep(1)