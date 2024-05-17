from dotenv import load_dotenv
import os
import requests
import time

from scraper import BBC
from mail import send_email

load_dotenv()
API_KEY = os.environ.get("NEWS_API_KEY", None)
URL = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}"


def fetch_news():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        news_data = response.json()

        if news_data.get("status") == "ok":
            print(f"News fetched at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            articles = news_data.get("articles", [])
            for article in articles:
                Description = article.get("description")
                Title = article.get("title")
                print(f"Title: {article.get('title')}")
                print(f"Description: {article.get('description')}")
                print(f"URL: {article.get('url')}")
                print(f"Published At: {article.get('publishedAt')}")
                print("-" * 40)
                send_email(subject=Title, body=Description)

        else:
            print("Failed to fetch news:", news_data.get("message"))

    except requests.exceptions.RequestException as e:
        print("Error fetching news:", e)


def main():
    fetch_news()


if __name__ == "__main__":
    main()
