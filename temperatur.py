"""
Modul zur Verwaltung von Temperaturdaten in einer MySQL-Datenbank.

Dieses Modul enthält Funktionen zum Einfügen von Temperaturen
und zum Abrufen der gespeicherten Daten.
"""

import mysql.connector
from mysql.connector import Error

# Konstanten für die Datenbankverbindung
DB_HOST = 'localhost'
DB_NAME = 'heizungsdaten'
DB_USER = 'root'
DB_PASSWORD = 'infolab'


def insert_temperatures(data_to_insert):
    """
    Löscht alle bestehenden Einträge in der Tabelle `temperatur`
    und fügt die neuen Temperaturdaten ein.

    Args:
        data_to_insert (dict): Ein Dictionary mit Datum als Schlüssel
                               und Temperaturwerten als Wert.
    """
    conn = None
    cursor = None
    try:
        # Verbindung zur Datenbank herstellen
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Alle bestehenden Einträge löschen
        delete_query = "DELETE FROM temperatur"
        cursor.execute(delete_query)
        conn.commit()
        print(f"{cursor.rowcount} bestehende Einträge wurden gelöscht.")

        # Neue Daten einfügen
        data_as_tuples = list(data_to_insert.items())
        insert_query = """
        INSERT INTO temperatur (Datum, Mindesttemperatur)
        VALUES (%s, %s)
        """
        cursor.executemany(insert_query, data_as_tuples)
        conn.commit()
        print(f"{cursor.rowcount} neue Einträge wurden erfolgreich hinzugefügt.")

    except Error as error:
        # Fehlerbehandlung
        print(f"Fehler bei der Datenbankoperation: {repr(error)}")

    finally:
        # Ressourcen freigeben
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


def fetch_temperatures():
    """
    Ruft alle Temperaturdaten aus der Tabelle `temperatur` ab.

    Returns:
        dict: Ein Dictionary mit Datum als Schlüssel (im ISO-Format)
              und Temperaturwerten als Wert.
    """
    conn = None
    cursor = None
    try:
        # Verbindung zur Datenbank herstellen
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Daten abrufen
        select_query = "SELECT Datum, Mindesttemperatur FROM temperatur"
        cursor.execute(select_query)
        records = cursor.fetchall()

        # Daten als Dictionary formatieren
        temperature_dict = {row[0].strftime('%Y-%m-%d'): row[1] for row in records}
        return temperature_dict

    except Error as error:
        # Fehlerbehandlung
        print(f"Fehler bei der Datenabfrage: {repr(error)}")
        return {}

    finally:
        # Ressourcen freigeben
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
