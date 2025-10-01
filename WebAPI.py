import requests


#Dokumentation: https://docs.coingecko.com/docs/sdk

web_url = "https://api.geckoterminal.com/api/v2/networks"
graph_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=2025-01-01&to=2025-08-10&x_cg_demo_api_key=CG-kGgB4jzBXM8qNe4is6PitM4f"
response = requests.get(web_url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()   # JSON in Python-Daten umwandeln
    print(data)              
else:
    print("Fehler:", response.status_code)
    
    
    
coin = input("Welcher coin: ")
coins_url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&ids={coin}&x_cg_demo_api_key=CG-kGgB4jzBXM8qNe4is6PitM4f"


