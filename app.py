from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random

app = Flask(__name__)

@app.before_request
def before_request():
    global db
    db = sqlite3.connect('urls.db')
    global c
    c = db.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS Urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT NOT NULL UNIQUE,
            created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)
    ''')
    db.commit()

# Function to generate a short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()

        # Check if the original URL already exists in the database
        c.execute('SELECT * FROM Urls WHERE original_url = ?', (original_url,))
        existing_url = c.fetchone()

        if existing_url:
            # If it exists, just get the short URL from the database
            short_url = existing_url[2]  # The short_url is the third column in the database
        else:
            # Otherwise, generate a new short URL and store it in the database
            short_url = generate_short_url()
            c.execute('INSERT INTO Urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
            conn.commit()

        conn.close()
        return render_template('home.html', short_url=request.host_url + short_url)


    return render_template('home.html')


@app.route('/<short_url>')
def redirect_to_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Urls WHERE short_url = ?', (short_url,))
    original_url = c.fetchone()[1]  # The original_url is the second column in the database
    conn.close()
    return redirect(original_url)

if __name__ == '__main__':
    app.run(debug=True)
