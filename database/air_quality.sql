CREATE TABLE AirQuality (
    id serial PRIMARY KEY,
    id_city_fk INT not null,
    date date NOT NULL,
    pm25 DECIMAL(5,2),
    pm10 DECIMAL(5,2),
    o3 DECIMAL(5,2),
    no2 DECIMAL(5,2),
    so2 DECIMAL(5,2),
    co DECIMAL(5,2),
    aqi INT, 
    AQI_Category VARCHAR(50),
    constraint fk_city 
    	foreign key(id_city_fk)
    	references City(id)
)