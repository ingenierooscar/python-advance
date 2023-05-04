import requests

url = "https://webhook.site/33a0e90c-de37-41ea-aef3-3ddf217a33a5"
payload = {"plato": "pasta", "canitdad": 2} 
query_params = {"nombre": "gono"}
response = requests.post(url, data= payload, params=query_params)
print(response.status_code)
print(response.text) #no da nada

