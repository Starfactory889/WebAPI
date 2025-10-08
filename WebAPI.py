import requests
import plotly.express as px
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Funktion zum Abrufen der verfügbaren Coins von gecko terminal
def get_coins():
    url = "https://api.geckoterminal.com/api/v2/networks"
    response = requests.get(url)
    if response.status_code == 200:
        # Ausgabe der gesamten JSON-Antwort für die Fehlersuche
        data = response.json()
        print(data)  # Zur Überprüfung der Struktur
        return [coin['id'] for coin in data['data']]  # Möglicherweise unter 'data'
    else:
        messagebox.showerror("Fehler", "Fehler beim Abrufen der Coins.")
        return []

# Funktion zum Abrufen der Preisdaten und Erstellen des Diagramms
def fetch_data():
    coin = coin_var.get()
    start_date = start_date_var.get()
    end_date = end_date_var.get()

    # Umwandlung der Daten
    start_ts = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp())
    end_ts = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp())

    graph_url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range?vs_currency=eur&from={start_ts}&to={end_ts}&precision=full"

    response = requests.get(graph_url)

    if response.status_code == 200:
        data = response.json()
        prices = data['prices']

        timestamps = [datetime.datetime.fromtimestamp(item[0] / 1000) for item in prices]
        values = [item[1] for item in prices]

        # Daten für Plotly Express vorbereiten
        df = {
            'Timestamp': timestamps,
            'Price': values
        }

        # Graph erstellen mit Plotly Express
        fig = px.line(df, x='Timestamp', y='Price', title=f'{coin.capitalize()} Preisentwicklung')
        fig.show()
    else:
        messagebox.showerror("Fehler", "Fehler beim Abrufen der Marktdaten.")

# GUI erstellen
root = tk.Tk()
root.title("Crypto Preisdiagramm")

# Variable für Coin
coin_var = tk.StringVar()
# Variable für Startdatum
start_date_var = tk.StringVar()
# Variable für Enddatum
end_date_var = tk.StringVar()

# Auswahl der Coins
available_coins = get_coins()
coin_label = ttk.Label(root, text="Wähle einen Coin:")
coin_label.pack()
coin_combobox = ttk.Combobox(root, textvariable=coin_var, values=available_coins)
coin_combobox.pack()

# Eingabefelder für die Datumsangaben
start_date_label = ttk.Label(root, text="Zeitraum Beginn (YYYY-MM-DD):")
start_date_label.pack()
start_date_entry = ttk.Entry(root, textvariable=start_date_var)
start_date_entry.pack()

end_date_label = ttk.Label(root, text="Zeitraum Ende (YYYY-MM-DD):")
end_date_label.pack()
end_date_entry = ttk.Entry(root, textvariable=end_date_var)
end_date_entry.pack()

# Schaltfläche zum Abrufen der Daten
fetch_button = ttk.Button(root, text="Daten Abrufen und Diagramm Anzeigen", command=fetch_data)
fetch_button.pack()

# Hauptschleife starten
root.mainloop()
