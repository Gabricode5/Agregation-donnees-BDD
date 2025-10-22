CREATE TABLE City (
    id serial PRIMARY KEY,
    city varchar(50), 
    latitude  DECIMAL(5,2) NOT NULL,
    longitude DECIMAL(5,2) NOT NULL
)
