import requests
#import plotly
import datetime



#Dokumentation: https://docs.coingecko.com/docs/sdk

web_url = "https://api.geckoterminal.com/api/v2/networks"
response = requests.get(web_url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()   # JSON in Python-Daten umwandeln
    print(data)              
else:
    print("Fehler:", response.status_code)
    
    
    
coin = input("Welcher coin: ")
coins_url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&ids={coin}&x_cg_demo_api_key=CG-kGgB4jzBXM8qNe4is6PitM4f"

Zeitraum_b = input("Zeitraum Beginn (YYYY-MM-DD): ")
Zeitraum_e = input("Zeitraum Ende (YYYY-MM-DD): ")

# YYYY-MM-DD -> Unix-Timestamp
start_ts = int(datetime.datetime.strptime(Zeitraum_b, "%Y-%m-%d").timestamp())
end_ts = int(datetime.datetime.strptime(Zeitraum_e, "%Y-%m-%d").timestamp())

graph_url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range?vs_currency=eur&from={start_ts}&to={end_ts}&precision=full&interval=daily&x_cg_demo_api_key=CG-kGgB4jzBXM8qNe4is6PitM4f"

data = response.json()   # JSON in Python-Daten umwandeln
print(data)




