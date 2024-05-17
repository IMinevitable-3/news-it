# News Summarizer and Emailer

This Python project fetches top news headlines from the BBC News using the NewsAPI, summarizes the articles, and sends the summaries via email to specified recipients. The script uses a scheduler to run at a specified interval (e.g., every hour) to keep the recipients updated with the latest news.

## Features

- Fetches top news headlines from BBC News.
- Summarizes the news articles.
- Sends summarized news articles via email.
- Scheduled to run at regular intervals.

## Prerequisites

- Python 3.6 or higher
- An API key from [NewsAPI](https://newsapi.org/)
- A Gmail account for sending emails (ensure "Less secure app access" is enabled or use an App Password if 2-Step Verification is enabled)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/news-summarizer-emailer.git
   cd news-summarizer-emailer
   ```
