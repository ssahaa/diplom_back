import requests

def getTP():
    data = requests.get('http://127.0.0.1:8000/ТП/')
    GostData = data.json()
    return GostData
