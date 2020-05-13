# Makes a request to the broker URL changing the value at topic "light"
import requests

def getLight():
    url = ''
    res = requests.get(url)
    if res.status_code != 200:
        print('Request code: ', res.status_code)
    return res.text

def setLight(light_state):
    url = ''
    if str(light_state) != getLight():
        res = requests.post(url, json=light_state)
        if res.status_code != 200:
            print('Request code: ', res.status_code)