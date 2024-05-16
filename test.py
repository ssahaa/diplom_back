import requests

url = "http://127.0.0.1:8000/Согласование%20ТП/"

with open('D:\Шаблон ТП.docx', 'rb') as file:
    file_data = file.read()

files = {
    'dock': ('123', file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
}

data = {
    "comment": "Тест",
    "commentOLD": "No old comment",
    "creator": 2,
    "idTpStringNew": "123"
}

r = requests.post(url, files=files, data=data)

print(r.status_code, r.text)
