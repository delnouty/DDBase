import sqlite3
import csv

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table "clients"
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    client_ID INTEGER UNIQUE,
    Nom TEXT,
    Prénom TEXT,
    Email TEXT,
    Téléphone NUMERIC,
    Date_Naissance DATE,
    Adresse TEXT,
    Consentement_Marketing BOOLEAN,
    PRIMARY KEY(client_ID),
    FOREIGN KEY (client_ID) REFERENCES Commande(Client_ID)
    ON UPDATE NO ACTION ON DELETE NO ACTION
)
''')

# Create table "Commande"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Commande (
    Commande_ID INTEGER NOT NULL UNIQUE,
    Client_ID INTEGER,
    Date_Commande DATE,
    Montant_Commande REAL,
    PRIMARY KEY(Commande_ID)
)
''')

# Function to fill the clients table with data from CSV file
def fill_clients_table(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        print("CSV Headers:", headers)  # Print the headers to check for discrepancies
        next(reader)  # Skip the first line
        for row in reader:
            cursor.execute('''
                INSERT OR IGNORE INTO clients (client_ID, Nom, Prénom, Email, Téléphone, Date_Naissance, Adresse, Consentement_Marketing)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (row['client_ID'], row['Nom'], row['Prénom'], row['Email'], row['Téléphone'], row['Date_Naissance'], row['Adresse'], row['Consentement_Marketing']))
    conn.commit()

# Function to fill the Commande table with data from CSV file
def fill_commande_table(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        next(reader)  # Skip the first line
        for row in reader:
            cursor.execute('''
                INSERT OR IGNORE INTO Commande (Commande_ID, Client_ID, Date_Commande, Montant_Commande)
                VALUES (?, ?, ?, ?)
            ''', (row['Commande_ID'], row['Client_ID'], row['Date_Commande'], row['Montant_Commande']))
    conn.commit()

# Full paths to the CSV files
clients_csv_path = r'C:\Users\darya\Documents\Simplon\DDBase\SecondExr\jeu-de-donnees-clients.csv'
commandes_csv_path = r'C:\Users\darya\Documents\Simplon\DDBase\SecondExr\jeu-de-donnees-commandes.csv'

# Call the functions to fill the tables
fill_clients_table(clients_csv_path)
fill_commande_table(commandes_csv_path)

# Close the connection
conn.close()

print("Tables created and data inserted successfully.")
