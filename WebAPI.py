import requests


#Dokumentation: https://docs.coingecko.com/docs/sdk
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&x_cg_demo_api_key=CG-kGgB4jzBXM8qNe4is6PitM4f"
web_url = "https://api.geckoterminal.com/api/v2/networks"
response = requests.get(web_url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()   # JSON in Python-Daten umwandeln
    print(data)              
else:
    print("Fehler:", response.status_code)
    