CREATE TABLE IF NOT EXISTS "clients" (
	"client_ID" INTEGER UNIQUE,
	"Nom" TEXT,
	"Prénom" TEXT,
	"Email" TEXT,
	"Téléphone" NUMERIC,
	"Date_Naissance" DATE,
	"Adresse" TEXT,
	"Consentement_Marketing" BOOLEAN,
	PRIMARY KEY("client_ID"),
	FOREIGN KEY ("client_ID") REFERENCES "Commande"("Client_ID")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "Commande" (
	"Commande_ID" INTEGER NOT NULL UNIQUE,
	"Client_ID" INTEGER,
	"Date_Commande" DATE,
	"Montant_Commande" REAL,
	PRIMARY KEY("Commande_ID", "Client_ID")
);
