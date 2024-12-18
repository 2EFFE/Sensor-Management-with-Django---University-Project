from . import views
from django.urls import path

#reindirizzamenti
urlpatterns = [
    path('', views.index, name = 'elencoSensori'),
    path('<int:sensoreID>/', views.dettaglioSensore, name = 'dettaglioSensore'),
    path('api/letture/', views.aggiungiLettura, name = 'aggiungiLettura'),
]