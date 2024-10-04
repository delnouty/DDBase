import sqlite3
import pandas as pd

# File paths for the CSV files
clients_csv_path = './SecondEXr/clients.csv'
commandes_csv_path = './SecondExr/commandes.csv'

# Define the column names for the CSV files
clients_columns = ['Client_ID', 'Nom', 'Prénom', 'Email', 'Téléphone', 'Date_Naissance', 'Adresse', 'Consentement_Marketing']
commandes_columns = ['Commande_ID', 'Client_ID', 'Date_Commande', 'Montant_Commande']

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Enable foreign key support in SQLite
cursor.execute('PRAGMA foreign_keys = ON')

# Create table "clients" first
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    Client_ID INTEGER UNIQUE,
    Nom TEXT,
    Prénom TEXT,
    Email TEXT,
    Téléphone NUMERIC,
    Date_Naissance DATE,
    Adresse TEXT,
    Consentement_Marketing BOOLEAN,
    PRIMARY KEY(Client_ID)
)
''')

# Create table "Commande" with a foreign key referencing "clients"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Commande (
    Commande_ID INTEGER NOT NULL UNIQUE,
    Client_ID INTEGER,
    Date_Commande DATE,
    Montant_Commande REAL,
    PRIMARY KEY(Commande_ID),
    FOREIGN KEY (Client_ID) REFERENCES clients(Client_ID)
    ON UPDATE NO ACTION ON DELETE NO ACTION
)
''')

# Read CSV files into DataFrames, skipping the first row and using the correct headers
clients_df = pd.read_csv(clients_csv_path, skiprows=1, names=clients_columns)
commandes_df = pd.read_csv(commandes_csv_path, skiprows=1, names=commandes_columns)

# Remove duplicate Client_IDs
clients_df = clients_df.drop_duplicates(subset=['Client_ID'])

# Insert data into the tables
clients_df.to_sql('clients', conn, if_exists='append', index=False)
commandes_df.to_sql('Commande', conn, if_exists='append', index=False)

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()

print("Tables created and data inserted successfully.")
