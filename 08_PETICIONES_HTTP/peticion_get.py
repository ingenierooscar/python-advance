import requests

response = requests.get("https://api.github.com")
print(response)
print(response.headers)
print(response.status_code)

#datos de la respuesta o payload
print(response.content) #bytes
print(response.text)
print(response.json)
print(response.json()["current_user_url"])

#filtrar info query params
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python"}
) 
print(response.status_code)
print(response.json())

data = response.json()
print(data.keys)
