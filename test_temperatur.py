"""
Testmodul für die Temperaturdatenbank.

Dieses Modul testet die Funktionen `insert_temperatures` und `fetch_temperatures`
der Temperaturdatenbank.
"""

from datetime import datetime, timedelta
import pytest
from temperatur import insert_temperatures, fetch_temperatures


def get_next_seven_days_dict():
    """
    Erstellt ein Dictionary mit den nächsten 7 Tagen im ISO-Datumsformat
    als Schlüssel und float-Werten als Wert.

    Returns:
        dict: Ein Dictionary mit Datum als Schlüssel und Temperaturwerten.
    """
    return {
        (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'): i + 0.5
        for i in range(7)
    }


@pytest.mark.parametrize("expected_data", [get_next_seven_days_dict()])
def test_insert_temperatures(expected_data):
    """
    Testet das Einfügen und Abrufen von Temperaturen in der Datenbank
    im ISO-Datumsformat.

    Args:
        expected_data (dict): Ein Dictionary mit erwarteten Temperaturdaten.
    """
    # Daten in die Datenbank einfügen
    insert_temperatures(expected_data)

    # Daten aus der Datenbank abrufen
    returned_data = fetch_temperatures()

    # Überprüfen, ob die Daten korrekt eingefügt und zurückgegeben wurden
    assert expected_data == returned_data, (
        f"Erwartet: {expected_data}, Erhalten: {returned_data}"
    )
