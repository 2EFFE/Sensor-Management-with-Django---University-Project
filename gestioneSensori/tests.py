from django.test import TestCase
from django.urls import reverse
from gestioneSensori.models import Sensori, Letture

class SensoriTestCase(TestCase):
    def setUp(self): #inizializza i dati
        # Crea un sensore per i test
        self.sensor = Sensori.objects.create(
            id=1,
            tipo="Temperatura",
            descrizione='Sensore Temperatura',
            accuratezza=0.1,
            precisione=0.1,
            temperaturamin=0.0,
            temperaturamax=100.0,
            tolleranza=0.5,
            tensioneesercizio=12.0,
            sensibilita=0.2
        )

    def test_sensor_creation(self):
        """Testa che il sensore sia creato correttamente."""
        self.assertEqual(Sensori.objects.count(), 1) #conteggio dei sensori = 1
        self.assertEqual(self.sensor.tipo, "Temperatura")
        self.assertEqual(self.sensor.descrizione, 'Sensore Temperatura')
        self.assertEqual(self.sensor.accuratezza, 0.1)
        self.assertEqual(self.sensor.precisione, 0.1)
        self.assertEqual(self.sensor.temperaturamin, 0.0)
        self.assertEqual(self.sensor.temperaturamax, 100.0)
        self.assertEqual(self.sensor.tolleranza, 0.5)
        self.assertEqual(self.sensor.sensibilita, 0.2)

    def test_sensor_list_view(self):
        """Testa che la lista dei sensori sia visualizzata correttamente."""
        response = self.client.get(reverse('elencoSensori')) #richiede la pagina dei sensori
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Temperatura")

    def test_sensor_detail_view(self):
        """Testa che la pagina di dettaglio di un sensore sia visualizzata correttamente."""
        response = self.client.get(reverse('dettaglioSensore', args=[self.sensor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sensore Temperatura")

    def test_add_reading_invalid_sensor(self):
        """Testa che non sia possibile aggiungere una lettura per un sensore non esistente."""
        response = self.client.post(reverse('aggiungiLettura'), {
            'sensoreid': 999,  # ID sensore non esistente
            'valore': 25.0,
            'unita': 'C'
        })
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Letture.objects.count(), 0) #conteggio letture = 0

    def test_sensor_readings(self):
        """Testa che le letture di un sensore siano visualizzate correttamente."""
        Letture.objects.create(id=1, valore=30.0, unita='C', sensoriid=self.sensor)
        Letture.objects.create(id=2, valore=35.0, unita='C', sensoriid=self.sensor)

        response = self.client.get(reverse('dettaglioSensore', args=[self.sensor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "30.0")
        self.assertContains(response, "35.0")