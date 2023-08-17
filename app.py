from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_database_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect('soldiers.db')
    return conn

def fetch_records_from_database():
    """Fetch records from the 'soldiers' table."""
    conn = get_database_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM soldiers')
    records = cursor.fetchall()
    
    conn.close()
    return records

@app.route('/')
def index():
    """Display the records from the 'soldiers' table on the index page."""
    records = fetch_records_from_database()
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
