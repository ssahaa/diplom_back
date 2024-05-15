import requests


def getUserDataID(ID):
    data = requests.get(f'http://127.0.0.1:8000/Пользователи/{ID}/')
    return data
    #if ID


