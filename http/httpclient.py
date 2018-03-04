import requests
resp = requests.get("http://localhost:8080/qin/map/test")
print(resp.status_code)
print(resp.text)
print(resp.json())

reqParams = {'username':'fuyongde', 'password':'fuyongde'}
respParams = requests.get("http://localhost:8080/qin/map/testParams", params=reqParams)
print(respParams.status_code)
print(respParams.text)
print(respParams.json())