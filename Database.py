import sqlite3

def create_table():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Urls (original_url TEXT, short_url TEXT)')
    conn.commit()
    conn.close()

create_table()
