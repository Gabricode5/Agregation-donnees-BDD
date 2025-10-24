#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:05:03 2025

@author: nadya
"""

import requests
from bs4 import BeautifulSoup

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
table = soup.find("table")

# Initialisation d'une liste pour stocker les résultats
capitals = []

# Parcours des lignes du tableau (en ignorant l’en-tête)
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols) >= 4:
        capital = cols[2].get_text(strip=True)
        population = cols[3].get_text(strip=True)
        capitals.append((capital, population))

# Affichage des capitales et de leur population
for capital, population in capitals:
    print(f"{capital}: {population}")
