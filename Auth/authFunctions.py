import requests
def isCurrentLogin(login = 0, password = 0):
    data = requests.get('http://127.0.0.1:8000/Пользователи/')

    for i in range(len(data.json())):
        if data.json()[i]['login'] == login:
            if data.json()[i]['password'] == password:
                return True
    return False

def isAdministrator(login = 0, password = 0):
    data = requests.get('http://127.0.0.1:8000/Пользователи/')

    for i in range(len(data.json())):
        if data.json()[i]['login'] == login:
            if data.json()[i]['password'] == password:
                if data.json()[i]['WorkerGrade'] == 1 or data.json()[i]['WorkerGrade'] == 2:
                    return True
    return False