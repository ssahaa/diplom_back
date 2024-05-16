import requests

def getGOST():
    data = requests.get('http://127.0.0.1:8000/ГОСТ/')
    GOSTs = data.json()
    return GOSTs