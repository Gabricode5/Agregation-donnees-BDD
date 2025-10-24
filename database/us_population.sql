CREATE TABLE US_Population (
    id serial PRIMARY KEY,
    ville INT NOT NULL,
    capital VARCHAR(50) NOT NULL,
    population INT,
    FOREIGN KEY (ville) REFERENCES City (id)
);