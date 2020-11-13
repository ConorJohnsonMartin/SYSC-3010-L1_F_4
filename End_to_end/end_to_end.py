import requests
import json
import urllib.parse
import http.client
import time

#Lab2Part3
key = "H8QD218BNTIQL7OQ"
def readServerRPi():
    URL='https://api.thingspeak.com/channels/1155565/feeds.json?api_key=8JDWE6GONX7QWNAR&results=2'
    KEY='8JDWE6GONX7QWNAR'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    get_data=requests.get(NEW_URL).json()
    channel_id=get_data['channel']['id']
    field_1=get_data['feeds']
    return (field_1)

def transmission():
    while True:
        moisture = 1
        params = urllib.parse.urlencode({'field1': moisture, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (moisture)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

if __name__ == '__main__':
    readServerRPi()











            
