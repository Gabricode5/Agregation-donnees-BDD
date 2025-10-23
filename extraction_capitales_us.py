#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 08:05:03 2025

@author: nadya
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Trouver les tables de type wikitable
tables = soup.find_all("table", {"class": "wikitable"})
print(f"🔍 {len(tables)} tables trouvées sur la page.")

# Sélectionner la table des capitales d'état
table = tables[1]  # généralement la deuxième table

rows = table.find_all("tr")
data = []

for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 4:
        state = cols[0].text.strip()
        capital = cols[1].text.strip()
        population = cols[3].text.strip().split("[")[0]  # enlever les notes
        # Nettoyer population
        population = population.replace(",", "").replace("–", "0")
        try:
            population = int(population)
        except:
            population = 0
        data.append([state, capital, population])

# Créer DataFrame
df = pd.DataFrame(data, columns=["État", "Capitale", "Population"])
df = df.sort_values(by="Population", ascending=False).reset_index(drop=True)

# Sauvegarder CSV
df.to_csv("capitales_us_population_correct.csv", index=False, encoding="utf-8")

print("Données extraites avec succès !")
print(df.head(10))
