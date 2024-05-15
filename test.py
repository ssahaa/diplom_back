        
import requests
import os




url = "http://127.0.0.1:8000/media/TP/%D0%A2%D0%B5%D1%85_%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81_%D0%9D%D0%B0_%D1%80%D1%83%D1%87%D0%BA%D1%83.docx"
print(url)
save_path = 'D:\games'
print(save_path)
response = requests.get(url)
if response.status_code == 200:
    file_path = os.path.join(save_path, "ТП" + " " + '123' + ".docx")
    with open(file_path, "wb") as file:
        # Записываем содержимое файла
        file.write(response.content)
        file.close()