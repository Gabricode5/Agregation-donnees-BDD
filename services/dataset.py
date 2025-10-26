
# Importation de la librairie pandas pour manipuler des données sous forme de tableau
import pandas as pd

#Tentative d'ouverture du fichier CSV
# Si le fichier n'existe pas, on affiche un message d'erreur et on quitte le programme
try:
    df = pd.read_csv("C:/Users/marim/Downloads/archive (4)/Air_Quality_Data.csv")
except FileNotFoundError:
    print("le fichier est introuvable")
    exit()

# Affiche le nombre de lignes et de colonnes dans le fichier (shape = (nb_lignes, nb_colonnes))
print("afficher le nombre de ligne et des colonne", df.shape)

# Affiche le nom de toutes les colonnes
print("le nom des colonne", df.columns)

# Donne des informations générales sur le DataFrame (types, nombre de valeurs non nulles, mémoire)
print("============= les infos de base =================")
print(df.info())  #  pas besoin de print ici normalement, df.info() affiche déjà tout seul

#Compte le nombre de valeurs non nulles dans chaque colonne
print("============= non les valeurs manquantes =================")
print(df.count())

# Compte le nombre de valeurs manquantes dans chaque colonne
print("============= les valeurs manquantes =================")
print(df.isna().sum())

#  Statistiques de base sur les colonnes numériques (moyenne, min, max, etc.)
print(df.describe())

# Affiche la liste des villes avec latitude et longitude
# Ici, on utilise trois .unique() séparés => il y a un risque de décalage entre les colonnes !
print("============= afficher les city =================")
for ville, latitude, longitude in zip(df["city"].unique(), df["latitude"].unique(), df["longitude"].unique()):
    print(ville, "=> { latitude: ", latitude, ", longitude:", longitude, "}")

#Création d'une petite table "city_df" contenant une liste unique des villes et un ID
# Même problème ici : les .unique() ne garantissent pas le bon alignement entre les colonnes.
city_df = pd.DataFrame({
    "city": df["city"].unique(),
    "latitude": df["latitude"].unique(),
    "longitude": df["longitude"].unique(),
    "id": list(range(1, df["city"].nunique() + 1))  # création d'un ID unique pour chaque ville
})

# Création d'une liste pour stocker l'ID de la ville correspondant à chaque ligne du df principal
cities_ids = []

# On parcourt chaque ligne du DataFrame principal
for idx, ligne in df.iterrows():
    # On récupère l'ID de la ville qui correspond à la ville de cette ligne
    id_ville = list(city_df[city_df["city"] == df.iloc[idx]["city"]]["id"].unique())[0]
    cities_ids.append(id_ville)

#  On ajoute la colonne 'id_city_fk' au df principal (clé étrangère)
df["id_city_fk"] = cities_ids

# On supprime les colonnes inutiles ou qu'on a déplacées dans une autre table (city_df)
df = df.drop(columns=[
    'city', 'latitude', 'longitude', 'temperature_c', 'humidity_percent',
    'wind_speed_mps', 'month', 'day', 'year', 'day_of_week', 'hour',
    'is_weekend', 'day_of_year', 'season'
])

# On enregistre le DataFrame principal allégé dans un nouveau fichier CSV
df.to_csv("C:/Users/marim/Downloads/Air_Quality_out.csv", index=False)

# On enregistre la table des villes (ID + ville + coordonnées) dans un autre fichier CSV
city_df.to_csv("C:/Users/marim/Downloads/cities.csv", index=False)
