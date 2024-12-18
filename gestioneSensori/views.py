from django.shortcuts import render
from .models import Sensori, Letture
from django.db.models import Avg #avg = media
from io import BytesIO #Input e output byte
from rest_framework.decorators import api_view #gestisce le richieste HTTP tramite API
from rest_framework.response import Response #gestisce le richieste HTTP tramite API

 
import base64 #codificare i dati
import matplotlib.pyplot as plt #grafici


# Create your views here. 
def index(request): 
    sensori = Sensori.objects.all() #recupera un elenco di tutti i sensori
    return render(request, 'gestioneSensori/elencoSensori.html', {'sensori': sensori}) #mostra la pagina html


def dettaglioSensore(request, sensoreID):
    sensore = Sensori.objects.get(id = sensoreID) #seleziona sensore con ID specificato 
    letture = Letture.objects.filter(sensoriid = sensoreID) #seleziona tutte le letture appartententi al sensore con ID specificato

    if letture.exists():
        primaLettura = letture.earliest('datarilevazione')
        ultimaLettura = letture.latest('datarilevazione')
        mediaLettura = letture.aggregate(Avg('valore'))['valore__avg']

        # creazione del grafico
        valori = [lettura.valore for lettura in letture] #vettore con i valori delle letture selezionate
        timestamp = [lettura.datarilevazione for lettura in letture] #vettore con la data di rilevazione delle letture selezionate
        plt.figure(figsize=(10,5))
        plt.plot(timestamp, valori, marker = 'o') #grafico x, y, indicatore
        plt.title('Andamento letture')
        plt.xlabel('Tempo')
        plt.ylabel('Valore')
        plt.grid() #creazione definitiva

        #predisporre la mostra a video del grafico
        buffer = BytesIO() #buffer di byte
        plt.savefig(buffer, format = 'png') #salvataggio grafico in buffer
        buffer.seek(0) #riposiziona il puntamento all'inizio del buffer
        image = buffer.getvalue() #crea una variabile con il grafico completo
        buffer.close() 
        grafico = base64.b64encode(image).decode('utf-8') #codifico il grafico in base64 per ridurre le dimensioni 
    else:
        primaLettura = ultimaLettura = mediaLettura = grafico = None

    return render(request, 'gestioneSensori/dettaglioSensore.html', {
        'sensore' : sensore,
        'primaLettura' : primaLettura,
        'ultimaLettura' : ultimaLettura,
        'mediaLettura' : mediaLettura,
        'grafico' : grafico
    })

@api_view(['POST']) #riceve la richiesta e la gestisce
def aggiungiLettura(request):
    sensore_id = request.data.get('sensoreid') #recupera dalla richiesta HTTP i parametri
    valore = request.data.get('valore') #recupera dalla richiesta HTTP i parametri
    unita_di_misura = request.data.get('unita') #recupera dalla richiesta HTTP i parametri
    
    try:
        sensore = Sensori.objects.get(id=sensore_id) #recupera il sensore con ID sensore ID
        Letture.objects.create(valore=valore, unita=unita_di_misura, sensoriid=sensore) #inserisce nel database la lettura
        return Response({"message": "Lettura aggiunta con successo."}, status=201) #tutto ok
    except Sensori.DoesNotExist:
        return Response({"error": "Sensore non trovato."}, status=404) #errore
    except Exception:
        return Response({"error":"Generic Error"}, status=400)
        