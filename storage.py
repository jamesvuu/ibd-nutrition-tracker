"""Local SQLite storage. No cloud upload; never bundle real health records."""
import sqlite3
from datetime import date

SCHEMA = '''
CREATE TABLE IF NOT EXISTS meals (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 entry_date TEXT NOT NULL, food TEXT NOT NULL, calories INTEGER NOT NULL CHECK(calories >= 0),
 protein_g REAL NOT NULL DEFAULT 0 CHECK(protein_g >= 0), notes TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS symptoms (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 entry_date TEXT NOT NULL, symptom TEXT NOT NULL,
 severity INTEGER NOT NULL CHECK(severity BETWEEN 0 AND 10), notes TEXT NOT NULL DEFAULT ''
);
'''

def connect(path='tracker.db'):
    con = sqlite3.connect(str(path))
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con

def add_meal(con, day, food, calories, protein_g=0, notes=''):
    if not str(food).strip() or int(calories) < 0 or float(protein_g) < 0:
        raise ValueError('Provide a food name and non-negative nutrition values.')
    date.fromisoformat(str(day))
    con.execute('INSERT INTO meals(entry_date,food,calories,protein_g,notes) VALUES(?,?,?,?,?)', (str(day),str(food).strip(),int(calories),float(protein_g),str(notes)))
    con.commit()

def add_symptom(con, day, symptom, severity, notes=''):
    if not str(symptom).strip() or not (0 <= int(severity) <= 10):
        raise ValueError('Provide a symptom and severity between 0 and 10.')
    date.fromisoformat(str(day))
    con.execute('INSERT INTO symptoms(entry_date,symptom,severity,notes) VALUES(?,?,?,?)', (str(day),str(symptom).strip(),int(severity),str(notes)))
    con.commit()

def get_rows(con, table):
    if table not in ('meals','symptoms'):
        raise ValueError('Invalid table')
    return [dict(row) for row in con.execute(f'SELECT * FROM {table} ORDER BY entry_date DESC, id DESC')]
