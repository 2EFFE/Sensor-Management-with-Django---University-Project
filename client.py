import requests
import random
import time

URL = "http://localhost:8000/gestioneSensori/api/letture/" #URL di connessione
#creazione dati sensori
SENSORI = [
    {
        "id": 1, 
        "range_min": 0,
        "range_max": 3000,
        "unita": "ustrain"
    },
    {
        "id": 2, 
        "range_min": 2,
        "range_max": 400,
        "unita": "cm"
    },
    {
        "id": 3, 
        "range_min": 0,
        "range_max": 40,
        "unita": "°"
    },
    {
        "id": 4, 
        "range_min": 0.2,
        "range_max": 50,
        "unita": "m"
    },
    {
        "id": 5, 
        "range_min": -40,
        "range_max": 150,
        "unita": "°C"
    },
    {
        "id": 6, 
        "range_min": -245,
        "range_max": 245,
        "unita": "dps"
    },
    {
        "id": 7, 
        "range_min": 1,
        "range_max": 135,
        "unita": "dB"
    },
    {
        "id": 8, 
        "range_min": 0,
        "range_max": 1,
        "unita": ""
    },
    {
        "id": 9, 
        "range_min": 300,
        "range_max": 10000,
        "unita": "ppm"
    },
    {
        "id": 10, 
        "range_min": 0,
        "range_max": 0.8,
        "unita": "mg/m3"
    },
]

while True:
    sensoreId = int(round(random.uniform(1,10),0)) #seleziona un sensore causale
    rangeMax=SENSORI[sensoreId-1]["range_max"]
    rangeMin=SENSORI[sensoreId-1]["range_min"]
    valore = round(max(rangeMin, min(rangeMax, random.gauss((rangeMax+rangeMin)/2, (rangeMax-rangeMin)/6))), 2) #genera un valore casuale tra range_min e range_max e arrotonda a due cifre decimali
    if SENSORI[sensoreId-1]["unita"] == "": #se la stringa unità è vuota
        valore = int(valore)
    lettura = {
        "valore": valore,
        "unita": SENSORI[sensoreId-1]["unita"],
        "sensoreid": sensoreId
    }
    try:
        response = requests.post(URL, json=lettura)  #esegue una richiesta HTTP POST inviando i dati presenti in lettura
        print(f"Invio lettura: {lettura} - Status: {response.status_code}")
    except requests.exceptions.ConnectionError: # se si verifica un errore di connessione
        print("Impossibile stabilire la connessione con il server")

    time.sleep(10) #si ferma per 0.5 secondi
