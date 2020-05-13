# Makes a request to the broker URL changing the value at topic "light"
import requests

def getLight():
    url = 'http://03670640:a5b8237720ca6068@broker.shiftr.io/light'
    res = requests.get(url)
    if res.status_code != 200:
        print('Request code: ', res.status_code)
    return res.text

def setLight(light_state):
    url = 'http://03670640:a5b8237720ca6068@broker.shiftr.io/light'
    if str(light_state) != getLight():
        res = requests.post(url, json=light_state)
        if res.status_code != 200:
            print('Request code: ', res.status_code)