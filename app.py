from flask import Flask, jsonify, request
from retrieve_news import getArticles

app = Flask(__name__) # create new flask app
storage = getArticles("articles.db")

# define API endpoint (news) route for GET requests
@app.route("/news", methods=["GET"])
def get_news():
    subject = request.args.get("subject")
    source = request.args.get("source", "The Guardian") # default the guardian if not provided

    articles = storage.get_articles(subject, source)
    return jsonify({"articles": articles}) # return articles data in json

if __name__ == "__main__":
    app.run(debug=True)
