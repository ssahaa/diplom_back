import requests
url = f"http://127.0.0.1:8000/ТП/1/"
print(url)
data = {
"needForChange": False
}
r = requests.patch(url, data=data)
print(r.status_code)