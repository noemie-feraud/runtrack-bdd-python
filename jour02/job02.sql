CREATE TABLE etage (
    id INT AUTO_INCREMENT PRMARY KEY,
    nom VARCHAR(255),
    numero INT NOT NULL,
    superficie INT NOT NULL
);

CREATE TABLE salle (
    id INT AUTO_INCREMENT PRIMARY KEY
    nom VARCHAR(255),
    id_etage INT NOT NULL,
    capacite INT NOT NULL
);