#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 11:45:04 2025

@author: nadya
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL du site à scraper
url = "https://www.trailsunblazed.com/largest-state-capitals/"

# Ajout d'un en-tête User-Agent pour éviter le blocage 406
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}

# Envoi de la requête HTTP avec headers
response = requests.get(url, headers=headers)
response.raise_for_status()

# Analyse du contenu HTML
soup = BeautifulSoup(response.text, "html.parser")

# Recherche du tableau contenant les données
# Utilisation de find("table") car il n'y en a qu'un
table = soup.find("table")

# Initialisation d'une liste pour stocker les résultats [State, Population]
data = []

# Parcours des lignes du tableau (en ignorant l’en-tête, row[0])
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    
    # Vérification que nous avons au moins les 4 colonnes : Rank, State, City, Population
    if len(cols) >= 4:
        # Index 2 est la 'City' (State)
        state = cols[2].get_text(strip=True)
        # Index 3 est la 'Population'
        population = cols[3].get_text(strip=True)     
        data.append([state, population])

# Création du DataFrame
df = pd.DataFrame(data, columns=["State", "Population"])


# ----------------- EXPORTATION CSV -----------------
filename = "states_us_population.csv"
df.to_csv(filename, index=False, encoding="utf-8")

print("Données extraites avec succès !")
print(f"Le fichier '{filename}' a été créé.")
print("\nAperçu des données :")
print(df.head())