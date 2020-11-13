import requests
import json
import urllib.parse
import http.client
import time

key = "Q5NPX2FJ6JJ8JQI1"
def readServerRPi():
    URL = "https://api.thingspeak.com/channels/1160321/feeds.json?api_key=MREJ31CF94AK6GX4&results=2"
    KEY = "MREJ31CF94AK6GX4"
    HEADER = "&results=2"
    NEW_URL = URL + KEY + HEADER
    get_data = requests.get(NEW_URL).JSON()
    channel_id = get_data['channel']['id']
    field_1 = get_data['feeds']
    return (field_1)

def transmission():
    while True:
        moisture = 1
        params = urllib.parse.urlencode({'field1': moisture, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        connection = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            connection.request("POST", "/update", params, headers)
            response = connection.getresponse()
            print (moisture)
            print (response.status, response.reason)
            data = response.read()
            connection.close()
        except:
            print ("connection failed")
        break

if __name__ == '__main__':
    readServerRPi()
