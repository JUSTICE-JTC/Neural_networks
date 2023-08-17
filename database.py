import sqlite3

def create_database(db_file):
    """Create a database connection and table."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS soldiers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birthplace TEXT,
        military_unit TEXT
    )
    '''
    cursor.execute(create_table_query)
    
    conn.commit()
    conn.close()

def insert_data(db_file, data):
    """Insert data into the soldiers table."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    insert_query = 'INSERT INTO soldiers (name, birthplace, military_unit) VALUES (?, ?, ?)'
    cursor.executemany(insert_query, data)
    
    conn.commit()
    conn.close()

def main():
    db_file = 'soldiers.db'
    data = [('John Smith', 'New York', '1st Infantry Division'),
            ('Jane Doe', 'Boston', '2nd Armored Division')]
    
    create_database(db_file)
    insert_data(db_file, data)
    
    print("Database created and data inserted successfully.")

if __name__ == '__main__':
    main()
