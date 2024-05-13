import requests


def iscurrentLogin(login = 0, password = 0):
    data = requests.get('http://127.0.0.1:8000/Пользователи/')

    print(len(data.json()))
    for i in range(len(data.json())):
        if data.json()[i]['login'] == login:
            if data.json()[i]['password'] == password:
                return True
    return False


if __name__ == "__main__":
    print(iscurrentLogin("Login123","pass123" ))