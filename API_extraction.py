# -*- coding: utf-8 -*-
import requests
import pandas as pd

API_KEY = "" #clé API OpenWeatherMap



# Liste des grandes villes françaises
villes = [
   "Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne", "Washington"
] #Liste des villes à analyser

meteo_data = []
count = 0

for ville in villes:
    # Appel API Nominatim pour récupérer latitude et longitude
    geocoding_url = f"https://nominatim.openstreetmap.org/search?q={ville},France&format=json&limit=1" #URL API Nominatim
    headers = {'User-Agent': 'AirQualityAnalysis/1.0'} #ajout d'un User-Agent pour respecter les conditions d'utilisation de Nominatim
    geo_response = requests.get(geocoding_url, headers=headers)
    
    if geo_response.status_code == 200: #vérification du succès de l'appel API géocodage
        geo_data = geo_response.json()
        if geo_data:
            latitude = geo_data[0].get('lat', 'N/A') #récupération de la latitude
            longitude = geo_data[0].get('lon', 'N/A') #récupération de la longitude

            
            if latitude != 'N/A' and longitude != 'N/A': #vérification de la présence des coordonnées
                weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric" #URL API OpenWeatherMap
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
            
            count += 1 #incrémentation de l'ID
            meteo_data.append({  
                'id': count,
                'ville': ville,
                'temperature_C': temperature,
                'humidite_pourcent': humidite,
                'pression_hPa': pression,
                'vitesse_vent_m_s': vitesse_vent,
                'conditions_meteo': conditions_meteo,
            }) #insertion des données dans la liste
    else:
        print(f"Erreur lors de l'appel API (code {geo_response.status_code})") #message d'erreur en cas d'échec de l'appel API

df = pd.DataFrame(meteo_data) #création du DataFrame pandas
df.to_csv("meteo_data.csv", index=False, encoding='utf-8-sig') #création du fichier csv
print("Export terminé : fichier 'meteo_data.csv' créé") #message de confirmation
