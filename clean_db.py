import sqlite3

db_path = "articles.db"

def del_old_articles(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM articles WHERE date < date('now', '-5 days')")

    conn.commit()
    conn.close()

    print(f"Deleted {cursor.rowcount} old articles.")

if __name__ == "__main__":
    del_old_articles(db_path)