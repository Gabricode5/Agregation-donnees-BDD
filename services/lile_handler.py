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


city_df = pd.DataFrame({"city":df["city"].unique(),
                        "latitude":df["latitude"].unique(),
                       "longitude":df["longitude"].unique(),
                       "id":list(range(1,df["city"].nunique()+1))
                       })
cities_ids = []
for idx,ligne in df.iterrows():
    cities_ids.append(
        list(city_df[city_df["city"] == df.iloc[idx]["city"]]["id"].unique())[0]
        )

df["id_city_fk"] = cities_ids

df = df.drop(columns=['city' , 'latitude','longitude','temperature_c', 'humidity_percent',
'wind_speed_mps', 'month', 'day', 'year', 'day_of_week', 'hour',
'is_weekend', 'day_of_year', 'season'])

df.to_csv("C:/Users/marim/Downloads/Air_Quality_out.csv", index=False)
city_df.to_csv("C:/Users/marim/Downloads/cities.csv", index=False)
