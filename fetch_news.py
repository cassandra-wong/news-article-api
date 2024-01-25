import requests
import sqlite3
import yaml
from datetime import datetime, timedelta, date

# connect to guardian api and configurate paths
# https://open-platform.theguardian.com/explore/
base_url = "https://content.guardianapis.com/search"
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
api_key = config['guardian_api']['api_key']
subjects = ["economy", "sport", "politics"]
db_path = "articles.db"

# fetch articles from the guardian api for a given subject in the past 5 days
def fetch_articles(subject):
    to_date = date.today()
    from_date = to_date - timedelta(days=5)

    params = {
        "api-key": api_key,
        "section": subject,
        "from-date": from_date,
        "to-date": to_date,
        "page-size": 10,
        "show-fields": "bodyText"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        articles = response.json().get("response", {}).get("results", [])
        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles for {subject} on {from_date}: {e}")
        return []

# store the fetched articles in a SQLite db
def store_articles(subject, articles):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for article in articles:
        # format date to exclude time
        article_date = datetime.strptime(article['webPublicationDate'], "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = article_date.strftime("%Y-%m-%d")

        # check if article with a specific URL already exists in the db to avoid duplicate
        # fetchone returns the first row of results only
        # if it is non-None, it continues
        cursor.execute("SELECT id FROM articles WHERE url = ?", (article['webUrl'],))
        if cursor.fetchone():
            continue

        cursor.execute('''INSERT INTO articles (subject, date, url, title, content) 
                          VALUES (?, ?, ?, ?, ?)''', 
                          (subject, formatted_date, article['webUrl'], 
                           article['webTitle'], article['fields']['bodyText']))
    conn.commit()
    conn.close()

def main():
    for subject in subjects:
        articles = fetch_articles(subject)
        if articles: # if non-empty
            store_articles(subject, articles)

if __name__ == "__main__":
    main()
