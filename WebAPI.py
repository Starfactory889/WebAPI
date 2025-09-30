import requests

url = "https://api.geckoterminal.com/api/v2/networks" 
response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()   # JSON in Python-Daten umwandeln
    print(data)              # Ausgabe der API-Antwort
else:
    print("Fehler:", response.status_code)