# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings

class Sensori(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descrizione = models.CharField(db_column='Descrizione', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accuratezza = models.FloatField(db_column='Accuratezza', blank=True, null=True)  # Field name made lowercase.
    precisione = models.FloatField(db_column='Precisione', blank=True, null=True)  # Field name made lowercase.
    temperaturamin = models.FloatField(db_column='TemperaturaMin', blank=True, null=True)  # Field name made lowercase.
    temperaturamax = models.FloatField(db_column='TemperaturaMax', blank=True, null=True)  # Field name made lowercase.
    tolleranza = models.FloatField(db_column='Tolleranza', blank=True, null=True)  # Field name made lowercase.
    tensioneesercizio = models.FloatField(db_column='TensioneEsercizio', blank=True, null=True)  # Field name made lowercase.
    sensibilita = models.FloatField(db_column='Sensibilita', blank=True, null=True)  # Field name made lowercase.

    class Meta: #database esterno
        managed = settings.IS_TESTING
        db_table = 'Sensori'
        app_label = 'gestioneSensori'

class Letture(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    valore = models.FloatField(db_column='Valore', blank=True, null=True)  # Field name made lowercase.
    unita = models.CharField(db_column='Unita', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datarilevazione = models.DateTimeField(auto_now_add=True, db_column='DataRilevazione')  # Field name made lowercase.
    sensoriid = models.ForeignKey(Sensori, db_column='SensoriID', on_delete=models.CASCADE, null=False)  # Field name made lowercase.

    class Meta:
        managed = settings.IS_TESTING   #variabile impostata nel file settings.py da mettere a false in produzione
        db_table = 'Letture'
        app_label = 'gestioneSensori'