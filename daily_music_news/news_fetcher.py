"""Fetch music news from NewsAPI."""

import logging
import requests
from typing import Optional
from config import Config

logger = logging.getLogger(__name__)


class NewsAPIFetcher:
    """Fetches music news from NewsAPI.org."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the news fetcher.

        Args:
            api_key: NewsAPI key (uses Config if not provided)
        """
        self.api_key = api_key or Config.NEWSAPI_KEY
        self.base_url = Config.NEWSAPI_BASE_URL

    def fetch_music_news(self, query: str = "music", limit: int = 10) -> list[dict]:
        """Fetch latest music news.

        Args:
            query: Search query (default: "music")
            limit: Maximum number of articles to fetch

        Returns:
            List of article dictionaries
        """
        try:
            url = f"{self.base_url}/everything"
            params = {
                "q": query,
                "language": Config.NEWS_LANGUAGE,
                "sortBy": Config.NEWS_SORT_BY,
                "apiKey": self.api_key,
                "pageSize": limit,
            }

            logger.info(f"Fetching {limit} music news articles...")
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get("status") != "ok":
                error_msg = data.get("message", "Unknown error")
                logger.error(f"NewsAPI error: {error_msg}")
                raise Exception(f"NewsAPI error: {error_msg}")

            articles = data.get("articles", [])
            logger.info(f"✅ Successfully fetched {len(articles)} articles")

            return articles

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch news: {e}")
            raise

    def format_articles(self, articles: list[dict]) -> str:
        """Format articles as readable text for summarization.

        Args:
            articles: List of article dictionaries

        Returns:
            Formatted articles as string
        """
        formatted = "MUSIC NEWS ARTICLES:\n" + "=" * 50 + "\n\n"

        for i, article in enumerate(articles, 1):
            formatted += f"{i}. {article.get('title', 'No title')}\n"
            formatted += f"   Source: {article.get('source', {}).get('name', 'Unknown')}\n"
            formatted += f"   {article.get('description', 'No description')}\n"
            formatted += f"   URL: {article.get('url', 'N/A')}\n"
            formatted += "\n"

        return formatted


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetcher = NewsAPIFetcher()
    articles = fetcher.fetch_music_news(limit=5)
    print(fetcher.format_articles(articles))
