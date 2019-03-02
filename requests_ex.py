import requests

url = "http://www.goggle.com"
# response = requests.get(url)
#
# print(f"your request to {url} has status code {response.status_code}")

# print(response.text)

# api plain text call, this site returns just plain text
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "text/plain"})

print(response.text)  # 'str'

# api json call
response = requests.get(url, headers={"Accept": "application/json"})
print(type(response.text))

data = response.json()
print(type(data))  # 'dict'
print(data["joke"])
print(f"status: {data['status']}")


# using query strings
url = "https://icanhazdadjoke.com/search"
topic = input("Enter a topic: ")

params = {"term": topic, "limit": "1"}

response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params=params)

data = response.json()
print(data)
if data["results"]:
    print(data["results"][0]["joke"])
