import sqlite3

with sqlite3.connect('scooters.db') as connection:

    connection.execute('PRAGMA foreign_keys = 1')

    cursor = connection.cursor()

    # Создание таблицы Scooters
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Scooters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            color TEXT NOT NULL,
            type TEXT NOT NULL
        );
    """)