CREATE TABLE Pays ( 
    id_p INT NOT NULL,
    nom_p VARCHAR(50), 
    PRIMARY KEY (id_p) 
); 

CREATE TABLE Auteur ( 
    id_a INT NOT NULL, 
    nom_a VARCHAR (30), 
    prenom_a VARCHAR (30), 
    date_naissance_a DATE, 
    id_p INT NOT NULL, 
    FOREIGN KEY (id_p) REFERENCES Pays(id_p), 
    PRIMARY KEY (id_a) 
); 

CREATE TABLE TypeLivre ( 
    id_t INT NOT NULL, 
    libelle_t VARCHAR (30), 
    PRIMARY KEY (id_t) 
); 

CREATE TABLE Livre ( 
    id_l INT NOT NULL, 
    titre_l VARCHAR (254), 
    annee_l VARCHAR (4), 
    resume_l TEXT, 
    id_t INT NOT NULL, 
    FOREIGN KEY (id_t) REFERENCES TypeLivre(id_t), 
    PRIMARY KEY (id_l) 
); 

CREATE TABLE Rediger ( 
    id_a INT NOT NULL, 
    id_l INT NOT NULL, 
    FOREIGN KEY (id_a) REFERENCES Auteur(id_a), 
    FOREIGN KEY (id_l) REFERENCES Livre (id_l), 
    PRIMARY KEY (id_a, id_l) 
); 

CREATE TABLE Edition ( 
    id_ed INT NOT NULL, 
    nom_ed VARCHAR (254), 
    PRIMARY KEY (id_ed) 
); 

CREATE TABLE Exemplaire ( 
    ref_e VARCHAR(254) NOT NULL, 
    id_ed INT NOT NULL, 
    id_l INT NOT NULL, 
    FOREIGN KEY (id_ed) REFERENCES Edition (id_ed), 
    FOREIGN KEY (id_l) REFERENCES Livre(id_l), 
    PRIMARY KEY (ref_e) 
); 

CREATE TABLE Inscrit ( 
    id_i INT NOT NULL, 
    nom_i VARCHAR (30), 
    prenom_i VARCHAR (30), 
    date_naissance_i DATE, 
    rue_i VARCHAR(50), 
    ville_i VARCHAR(50), 
    cp_i VARCHAR (5), 
    tel_i VARCHAR(15), 
    tel_portable_i VARCHAR(15) ,
    email_i VARCHAR(100),
    PRIMARY KEY (id_i)
); 

CREATE TABLE Emprunt ( 
    id_em INT NOT NULL, 
    date_em DATE, 
    delais_em INT DEFAULT 0, 
    id_i INT NOT NULL, 
    ref_e VARCHAR (254) NOT NULL, 
    FOREIGN KEY (id_i) REFERENCES Inscrit(id_i), 
    FOREIGN KEY (ref_e) REFERENCES Exemplaire(ref_e), 
    PRIMARY KEY (id_em) 
);