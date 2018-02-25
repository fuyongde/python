import requests
resp = requests.get("http://localhost:8080/niki/index")
print(resp.status_code)
print(resp.text)
print(resp.json())