import requests
import plotly.express as px
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Funktion zum Abrufen der Top 100 Coins von CoinGecko
def get_top_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false" 
    response = requests.get(url) #json file in respone
    
    if response.status_code == 200: #wenn alles geht 
        data = response.json() #wandelt json datei in liste um
        coins = []
        coin_map = {}
        

        for item in data: #nimmt die Daten der json/List und wiest diese einzelnen variablen zu 
            coin_id = item["id"] 
            coin_name = item["name"]
            symbol = item["symbol"].upper()
            display_name = f"{coin_name} ({symbol})"
            coins.append(display_name)
            coin_map[display_name] = coin_id
        return coins, coin_map
    else:
        messagebox.showerror("Fehler", "Fehler beim Abrufen der Coin-Liste.")
        return [], {}

# Funktion zum Abrufen der Preisdaten und Erstellen des Diagramms
def fetch_data():
    coin_name = coin_var.get() #übernimmt falls ich beim coin was eingebe
    if coin_name not in coin_map:
        messagebox.showerror("Fehler", "Ungültige Auswahl.")
        return

    coin_id = coin_map[coin_name]
    start_date = start_date_var.get()
    end_date = end_date_var.get()

    try:
        start_ts = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp()) # wandelt das Datum in sekunden ab dem unix timstamb um 
        end_ts = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp())
        
    except ValueError:
        messagebox.showerror("Fehler", "Ungültiges Datumsformat. Verwende YYYY-MM-DD.")
        return

    graph_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range?vs_currency=eur&from={start_ts}&to={end_ts}&precision=full"
    response = requests.get(graph_url) #holt sich json file

    if response.status_code == 200: #gleich wie oben 
        data = response.json() #umwandeln in dictionary 
        
        prices = data.get("prices", []) #holt sich den wert beim keywort prices, und speichert diesen in eine liste 
        #prices aufbau: [[Zeitstempel in ms,Wert in eur],...]

        if not prices:
            messagebox.showinfo("Info", "Keine Preisdaten gefunden.")
            return

        timestamps = [datetime.datetime.fromtimestamp(item[0] / 1000) for item in prices] #wandelt timestamp von sekunden in ein Datum um
        values = [item[1] for item in prices] # gibt den wert des coins für den graphen aus

        df = {"Timestamp": timestamps, "Price": values} #variable für darstellung 

        fig = px.line(df, x="Timestamp", y="Price", title=f"{coin_name} Preisentwicklung (EUR)") #darstellung Diagramm 
        fig.show()
    else:
        messagebox.showerror("Fehler", "Fehler beim Abrufen der Marktdaten.")

# GUI erstellen
root = tk.Tk()
root.title("Crypto Preisdiagramm")

coin_var = tk.StringVar()
start_date_var = tk.StringVar()
end_date_var = tk.StringVar()

# Coins abrufen
available_coins, coin_map = get_top_coins()

coin_label = ttk.Label(root, text="Wähle einen Coin:")
coin_label.pack(pady=5)

coin_combobox = ttk.Combobox(root, textvariable=coin_var, values=available_coins, width=40)
coin_combobox.pack()

start_date_label = ttk.Label(root, text="Zeitraum Beginn (YYYY-MM-DD):")
start_date_label.pack(pady=5)
start_date_entry = ttk.Entry(root, textvariable=start_date_var)
start_date_entry.pack()

end_date_label = ttk.Label(root, text="Zeitraum Ende (YYYY-MM-DD):")
end_date_label.pack(pady=5)
end_date_entry = ttk.Entry(root, textvariable=end_date_var)
end_date_entry.pack()

fetch_button = ttk.Button(root, text="Daten Abrufen und Diagramm Anzeigen", command=fetch_data)
fetch_button.pack(pady=10)

root.mainloop()
