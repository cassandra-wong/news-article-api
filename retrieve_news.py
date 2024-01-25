import sqlite3

class getArticles:
    def __init__(self, db_path):
        self.db_path = db_path

    # filter articles based on subject and news source (default "The Guardian")
    def get_articles(self, subject=None, source="The Guardian"):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = "SELECT * FROM articles WHERE source = ?"
        params = [source]

        # if subject is specified, include it in the query
        # i.e., "SELECT * FROM articles WHERE source = 'The Guardian' AND subject = 'sports'"
        if subject:
            query += " AND subject = ?"
            params.append(subject)

        cursor.execute(query, params)
        articles = cursor.fetchall()
        conn.close()

        return articles
