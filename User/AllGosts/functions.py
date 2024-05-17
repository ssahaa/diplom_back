import requests

def getGost():
    data = requests.get('http://127.0.0.1:8000/ГОСТ/')
    GostData = data.json()
    return GostData
