from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import requests
import os

app = Flask(__name__)
CORS(app)

# Hugging Face sentiment model (state-of-the-art)
sentiment_model = pipeline("sentiment-analysis")

# Your NewsAPI key
NEWS_API_KEY = "22f1e70387464962ab77e88aa074812e"  # Replace with your key

def fetch_company_news(company, language="en"):
    """
    Fetch latest news headlines for a company using NewsAPI.
    Returns a list of headlines.
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": company,
        "language": language,
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("NewsAPI request failed:", e)
        return []

    data = response.json()
    articles = data.get("articles", [])
    headlines = [article.get("title", "") for article in articles if article.get("title")]
    return headlines

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    company = data.get("company")
    language = data.get("language", "en")  # Optional, default English

    if not company:
        return jsonify({"error": "Company name is required"}), 400

    # Fetch real news
    headlines = fetch_company_news(company, language)

    # Analyze sentiment
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    for headline in headlines:
        result = sentiment_model(headline)[0]
        label = result['label'].upper()
        if label == "POSITIVE":
            sentiment_counts["positive"] += 1
        elif label == "NEGATIVE":
            sentiment_counts["negative"] += 1
        else:
            sentiment_counts["neutral"] += 1

    return jsonify({
        "headlines": headlines,
        "sentiment": sentiment_counts
    })

if __name__ == "__main__":
    app.run(debug=True)
