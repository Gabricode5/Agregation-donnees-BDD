# -*- coding: utf-8 -*-
import pandas  as  pd 

try:
    df =pd.read_csv("C:/Users/marim/Downloads/archive (4)/Air_Quality_Data.csv")
except FileNotFoundError:
    print("le fichier est introuvable")
    exit()

print("afficher le nobre de ligne et des colonne",df.shape) 
print("le nom des colonne",df.columns)
print("============= les infos de base =================")
print(df.info())
print("============= non les valeurs manquantes =================")
print(df.count())
print("============= les valeurs manquantes =================")
print(df.isna().sum())

print(df.describe())
print("============= afficher les city =================")
for ville,latitude , longitude in zip(df["city"].unique(), df["latitude"].unique(), df["longitude"].unique()):
    print(ville, "=> { latitude: ", latitude, ", longitude:", longitude, "}")

df.to_csv("C:/Users/marim/Downloads/Air_Quality_out.csv", index=False)
