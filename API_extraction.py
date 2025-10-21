# -*- coding: utf-8 -*-
import requests
import pandas as pd

API_KEY = "16d9be4164db2a69a3d85f0d21a9ce9a"

# Liste des grandes villes françaises
villes_francaises = [
    "Paris","Marseille","Lyon","Toulouse","Nice",
    "Nantes","Strasbourg","Montpellier","Bordeaux","Lille","Rennes",
    "Reims","Le Havre","Saint-Étienne","Toulon","Grenoble","Dijon","Angers","Nîmes","Villeurbanne"
]

air_quality_data = []
count = 0

for ville in villes_francaises:
    # Appel API Nominatim pour récupérer latitude et longitude
    geocoding_url = f"https://nominatim.openstreetmap.org/search?q={ville},France&format=json&limit=1"
    headers = {'User-Agent': 'AirQualityAnalysis/1.0'}
    geo_response = requests.get(geocoding_url, headers=headers)
    
    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        if geo_data:
            latitude = geo_data[0].get('lat', 'N/A')
            longitude = geo_data[0].get('lon', 'N/A')

            
            if latitude != 'N/A' and longitude != 'N/A':
                weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric" #
                weather_response = requests.get(weather_url) #Appel API météo
                if weather_response.status_code == 200: #vérification du succès de l'appel API météo
                    weather_data = weather_response.json()
                    temperature = weather_data['main'].get('temp', 'N/A')
                    humidite = weather_data['main'].get('humidity', 'N/A')
                    pression = weather_data['main'].get('pressure', 'N/A')
                    vitesse_vent = weather_data['wind'].get('speed', 'N/A')
                    conditions_meteo = weather_data['weather'][0].get('description', 'N/A') #ajout de la récupération des variables
                else:
                    (weather_response.status_code) #message d'erreur en cas d'échec de l'appel API météo
            
            if latitude != 'N/A' and longitude != 'N/A': #Vérification de la validité des coordonnées
                air_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={API_KEY}" #URL API pour la qualité de l'air
                air_response = requests.get(air_url) #Appel API pour la qualité de l'air
                if air_response.status_code == 200: #Vérification du succès de l'appel API
                    air_data = air_response.json()
                    aqi = air_data['list'][0]['main'].get('aqi', 'N/A')
                    components = air_data['list'][0]['components']
                    pm2_5 = components.get('pm2_5', 'N/A')
                    pm10 = components.get('pm10', 'N/A')
                    no2 = components.get('no2', 'N/A')
                    o3 = components.get('o3', 'N/A')
                    co = components.get('co', 'N/A')
                    so2 = components.get('so2', 'N/A') #ajout de la récupération des variables
            
            count += 1 #incrémentation de l'ID
            air_quality_data.append({  
                'id': count,
                'ville': ville,
                'latitude': latitude,
                'longitude': longitude,
                'temperature_C': temperature,
                'humidite_pourcent': humidite,
                'pression_hPa': pression,
                'vitesse_vent_m_s': vitesse_vent,
                'conditions_meteo': conditions_meteo,
                'indice_qualite_air_aqi': aqi,
                'PM2_5_μg_m3': pm2_5,
                'PM10_μg_m3': pm10,
                'NO2_μg_m3': no2,
                'O3_μg_m3': o3,
                'CO_μg_m3': co,
                'SO2_μg_m3': so2,
            }) #insertion des données dans la liste
    else:
        print(f"Erreur lors de l'appel API (code {geo_response.status_code})") #message d'erreur en cas d'échec de l'appel API

df = pd.DataFrame(air_quality_data) #création du DataFrame pandas
df.to_csv("air_quality_data.csv", index=False, encoding='utf-8-sig') #création du fichier csv
print("Export terminé : fichier 'air_quality_data.csv' créé") #message de confirmation