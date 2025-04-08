CREATE TABLE IF NOT EXISTS profils (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    signe_zodiaque VARCHAR(50),
    competences TEXT
);
