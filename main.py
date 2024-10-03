import sqlite3
import csv
from datetime import date

def create_tables():
    try:
        print("Connecting to database...")
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        print("Connected to database")

        print("Creating table Clients...")
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clients (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            prenom TEXT,
            email TEXT,
            date_inscription DATE
        )
        ''')
        print("Table Clients created")

        print("Creating table Commandes...")
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Commandes (
            id INTEGER PRIMARY KEY,
            client_id INTEGER,
            produit TEXT,
            date_commande DATE,
            FOREIGN KEY (client_id) REFERENCES Clients(id)
        )
        ''')
        print("Table Commandes created")

        conn.commit()
        print("Changes committed")
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("Connection closed")

# 1. Sélectionner tous les clients
def select_all_clients():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clients")
    clients = cursor.fetchall()
    conn.close()
    return clients

# 2. Récupérer les commandes d'un client spécifique
def get_orders_by_client(client_id):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Commandes WHERE client_id = ?", (client_id,))
    orders = cursor.fetchall()
    conn.close()
    return orders

# 3. Insérer des clients dans la base de données
def insert_clients():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    clients_data = [
        ('Doe', 'John', 'john.doe@example.com', date.today()),
        ('Smith', 'Jane', 'jane.smith@example.com', date.today())
    ]
    
    cursor.executemany("INSERT INTO Clients (nom, prenom, email, date_inscription) VALUES (?, ?, ?, ?)", clients_data)
    conn.commit()
    conn.close()
    print("2 clients added")

# 4. Insérer des commandes dans la base de données
def insert_orders():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    orders_data = [
        (1, 'Laptop', date.today()),  # Commande pour le client avec id = 1 (John Doe)
        (2, 'Smartphone', date.today())  # Commande pour le client avec id = 2 (Jane Smith)
    ]
    
    cursor.executemany("INSERT INTO Commandes (client_id, produit, date_commande) VALUES (?, ?, ?)", orders_data)
    conn.commit()
    conn.close()
    print("2 orders added")

# 5. Sauvegarder les résultats dans un fichier CSV
def save_to_csv(data, filename, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write the header row
        writer.writerows(data)  # Write the data rows
    print(f"Data saved to {filename}")

# Exemple d'utilisation
if __name__ == "__main__":
    create_tables()

    # Insérer deux clients et deux commandes
    insert_clients()
    insert_orders()

    # Sélectionner tous les clients et sauvegarder dans un fichier CSV
    clients = select_all_clients()
    save_to_csv(clients, 'clients.csv', ['ID', 'Nom', 'Prenom', 'Email', 'Date Inscription'])

    # Récupérer les commandes d'un client spécifique et sauvegarder dans un fichier CSV
    client_id = 1  # Exemple: client avec ID 1
    orders = get_orders_by_client(client_id)
    save_to_csv(orders, 'orders_client_1.csv', ['ID', 'Client_ID', 'Produit', 'Date Commande'])
