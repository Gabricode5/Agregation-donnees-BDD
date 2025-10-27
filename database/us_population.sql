CREATE TABLE US_Population (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    population INT,
    CONSTRAINT fk_city_population FOREIGN KEY (city_id) REFERENCES City (id)
);