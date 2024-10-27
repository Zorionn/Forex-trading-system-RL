import requests

def get_news_gnews(query, start_date, end_date, country="gb", language="en"):
    """
    Fetches news from GNews for a specified query and time range.
    
    :param query: Search keyword for the news topic
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :param country: Country code (e.g., 'us' for United States)
    :param language: Language code (e.g., 'en' for English)
    :return: JSON response with news articles
    """
    url = "https://gnews.io/api/v4/search"
    params = {
        "q": query,
        "from": start_date,
        "to": end_date,
        "country": country,
        "lang": language,
        "token": "f4eb4770c077d0104ce75d477904617a",
        "max": 100  # maximum number of articles to fetch per request
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

# Usage
start_date = "2017-01-01"
end_date = "2017-01-31"
query = "stock market"

news_data = get_news_gnews(query, start_date, end_date)
if news_data:
    articles = news_data.get("articles", [])
    for article in articles:
        print(f"{article['title']} - {article['publishedAt']}")
        print(article['url'])
        print()
