import json
import requests

url = "http://localhost:8080"
response = requests.get(url, headers={"Accept": "text/plain"})
print(response.text)  # 'str'


# response = requests.get(url, headers={"Accept": "text/plain"})

try:
    print(f"\n*** Get Todos***")
    url = "http://localhost:8080/todos"
    header = {"content-type": "application/json;charset=UTF-8", "accept": "application/json"
               }
    response = requests.get(url, headers=header)
    print(response.text)
    response.raise_for_status()
    response_json = response.json()
    print(json.dumps(response_json, indent=2))

except requests.exceptions.HTTPError as e:
    print(e)
    print(e.response.text)

url = "http://localhost:8080/todos/42"
response = requests.get(url, headers={"Accept": "text/plain"})
print(response.text)  # 'str'
