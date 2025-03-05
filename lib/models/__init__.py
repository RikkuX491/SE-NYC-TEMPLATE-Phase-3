import sqlite3

CONN = sqlite3.connect('data_structures.db')
CURSOR = CONN.cursor()