# News Article Aggregator API

The project uses the Flask web framework to create an API that serves news articles, stores data in a SQLite database, and includes a script for fetching news from The Guardian API.

## Usage

`create_db.py` creates a table stored in SQLite named articles.

`fetch_news.py` connects to the API, retrieves articles from the past five days for predefined subjects such as economy, sport, and politics, and stores them in a preexisting SQLite database. The script uses a YAML configuration file (`config.yaml`) to securely manage API keys and other settings. To run on your local machine, get a free API Key [here](https://open-platform.theguardian.com/access/) and enter your API in `config.yaml`:

   ```yaml
   guardian_api:
      api_key: "ENTER YOUR API KEY"
   ```

This script is typically run as part of the daily automated process but can also be executed independently to populate the database with the latest news articles.

`retrieve_news.py` features the `getArticles` class, which facilitates the retrieval of news articles from the SQLite database. It allows filtering articles based on subject and news source. The class method `get_articles` connects to the database, constructs a SQL query based on the specified parameters (subject and source), and fetches the corresponding articles.

`app.py` is a Flask web application that serves as the front end of the news aggregator. It defines an API endpoint `/news` for GET requests, allowing users to retrieve news articles stored in the SQLite database. Users can specify the `subject` and `source` (defaulting to "The Guardian") as query parameters in their requests. The script uses the `getArticles` class from `retrieve_news.py` to fetch articles matching these criteria. The articles are then returned in JSON format, making it easy for developers to integrate this API into various front-end applications or services. This Flask application can be started by running `python3 app.py` and is accessible via `http://localhost:5000/news`.

Sample Query:

```sh
http://localhost:5000/news?subject=politics
```

## Automated Daily Scraping with Local Cron Jobs

This project uses a local cron job to perform daily data scraping with the script `daily_news.sh`. It executes `fetch_news.py` to scrape the latest news articles and `clean_db.py` to remove outdated articles from the database that are over 5 days old.

To set up this cron job to be executed at midnight daily, add the following line to your crontab:

```bash
0 0 * * * ./daily_news.sh
```

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
