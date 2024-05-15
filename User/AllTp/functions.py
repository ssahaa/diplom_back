import requests

def getTp():
    data = requests.get('http://127.0.0.1:8000/ТП/')
    TpData = data.json()
    return TpData


def getOldTP():
    data = requests.get('http://127.0.0.1:8000/Старые%20ТП/')
    TpData = data.json()
    return TpData