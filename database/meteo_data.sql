CREATE TABLE meteo_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ville INT NOT NULL,
    temperature_C DECIMAL(5, 2),
    humidite_pourcent INT,
    pression_hPa INT,
    vitesse_vent_m_s DECIMAL(5, 2),
    conditions_meteo VARCHAR(255),
    date_collecte TIMESTAMP DEFAULT CURRENT_TIMESTAMP FOREIGN KEY (ville) REFERENCES City (id)
)