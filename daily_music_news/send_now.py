"""Send music news digest immediately (on-demand)."""

import logging
from datetime import datetime
from config import Config
from news_fetcher import NewsAPIFetcher
from summarizer import NewsSummarizer
from email_sender import GmailSender

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def send_digest_now():
    """Fetch news, summarize, and send email immediately."""
    try:
        logger.info("=" * 60)
        logger.info(f"🎵 Sending Music News Digest (On-Demand)")
        logger.info(f"Time: {datetime.now()}")
        logger.info("=" * 60)

        # Fetch news
        logger.info("📰 Fetching music news...")
        fetcher = NewsAPIFetcher()
        articles = fetcher.fetch_music_news(limit=10)

        if not articles:
            logger.error("No articles found")
            return False

        # Format articles
        formatted_articles = fetcher.format_articles(articles)

        # Summarize
        logger.info("🤖 Generating AI summary...")
        summarizer = NewsSummarizer()
        summary = summarizer.summarize(formatted_articles)

        # Create email body
        email_body = summarizer.create_email_body(summary)

        # Send email
        logger.info("📧 Sending email...")
        sender = GmailSender()
        success = sender.send_music_news_digest(email_body)

        if success:
            logger.info("=" * 60)
            logger.info("✅ Music news digest sent successfully!")
            logger.info(f"📧 Sent to: {Config.RECIPIENT_EMAIL}")
            logger.info("=" * 60)
            return True
        else:
            logger.error("Failed to send digest")
            return False

    except Exception as e:
        logger.error(f"Error: {e}")
        return False


if __name__ == "__main__":
    try:
        Config.validate()
        success = send_digest_now()
        exit(0 if success else 1)
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        exit(1)
