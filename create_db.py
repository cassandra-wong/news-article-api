import sqlite3

db_path = "articles.db"

def connect_to_db(path):
    conn = sqlite3.connect(path)
    return conn

def create_db_table(path):
    try:
        conn = connect_to_db(path)
        conn.execute('''
            CREATE TABLE articles (
                id INTEGER PRIMARY KEY NOT NULL,
                source TEXT DEFAULT 'The Guardian',
                subject TEXT NOT NULL,
                date TEXT NOT NULL,
                url TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("Table created successfully")
    except:
        print("Table creation failed")
    finally:
        conn.close()

if __name__ == "__main__":
    create_db_table(db_path)