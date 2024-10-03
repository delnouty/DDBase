-- 1. Creating the Clients table
CREATE TABLE IF NOT EXISTS Clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    prenom TEXT,
    email TEXT,
    date_inscription DATE
);

-- 2. Creating the Commandes table
CREATE TABLE IF NOT EXISTS Commandes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    produit TEXT,
    date_commande DATE,
    FOREIGN KEY (client_id) REFERENCES Clients(id)
);

-- 3. Inserting two clients into the Clients table
INSERT INTO Clients (nom, prenom, email, date_inscription)
VALUES 
    ('Doe', 'John', 'john.doe@example.com', DATE('now')),
    ('Smith', 'Jane', 'jane.smith@example.com', DATE('now'));

-- 4. Inserting two orders into the Commandes table
INSERT INTO Commandes (client_id, produit, date_commande)
VALUES 
    (1, 'Laptop', DATE('now')),
    (2, 'Smartphone', DATE('now'));

-- 5. Select all clients
SELECT * FROM Clients;

-- 6. Select all orders of a specific client (example with client_id = 1)
SELECT * FROM Commandes WHERE client_id = 1;

-- 7. Update the email address of a client (example for client_id = 1)
UPDATE Clients 
SET email = 'newemail@example.com' 
WHERE id = 1;

-- 8. Delete an order by id (example with order_id = 1)
DELETE FROM Commandes WHERE id = 1;

-- 9. Save query results to CSV file (SQLite CLI command)
-- The following commands are specific to the SQLite command-line tool and not standard SQL
.mode csv
.output clients_data_SQLite.csv
SELECT * FROM Clients;
.output stdout
