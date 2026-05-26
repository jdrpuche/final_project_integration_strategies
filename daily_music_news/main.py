"""Main application entry point."""

import logging
import time
import sys
from datetime import datetime
from config import Config
from news_fetcher import NewsAPIFetcher
from summarizer import NewsSummarizer
from email_sender import GmailSender
from scheduler import NewsScheduler

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("daily_music_news.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def fetch_and_summarize() -> str:
    """Fetch music news and generate a summary.

    Returns:
        HTML formatted summary
    """
    try:
        logger.info("=" * 60)
        logger.info(f"Starting news fetch and summarization at {datetime.now()}")
        logger.info("=" * 60)

        # Fetch news
        fetcher = NewsAPIFetcher()
        articles = fetcher.fetch_music_news(limit=10)

        if not articles:
            logger.warning("No articles found")
            return None

        # Format articles
        formatted_articles = fetcher.format_articles(articles)

        # Summarize
        summarizer = NewsSummarizer()
        summary = summarizer.summarize(formatted_articles)

        # Create email body
        email_body = summarizer.create_email_body(summary)

        logger.info("✅ Summary created successfully")
        return email_body

    except Exception as e:
        logger.error(f"Error in fetch_and_summarize: {e}")
        return None


def send_daily_digest():
    """Fetch news, summarize, and send email."""
    try:
        logger.info("🎵 Starting daily digest job...")

        # Fetch and summarize
        email_body = fetch_and_summarize()

        if not email_body:
            logger.error("Failed to generate summary")
            return

        # Send email
        sender = GmailSender()
        success = sender.send_music_news_digest(email_body)

        if success:
            logger.info("✅ Daily digest sent successfully!")
        else:
            logger.error("Failed to send digest email")

    except Exception as e:
        logger.error(f"Error in send_daily_digest: {e}")


def main():
    """Main application entry point."""
    logger.info("=" * 60)
    logger.info("Daily Music News Application Starting")
    logger.info("=" * 60)

    try:
        # Check for command-line arguments
        if len(sys.argv) > 1:
            if sys.argv[1] in ["--send-now", "-s", "send-now"]:
                # Send digest immediately
                logger.info("🚀 Send-Now Mode: Sending digest immediately...")
                Config.validate()
                send_daily_digest()
                logger.info("✅ Done!")
                return

        # Validate configuration
        Config.validate()
        logger.info("✅ Configuration validated")

        # Show settings
        logger.info(f"📧 Recipient: {Config.RECIPIENT_EMAIL}")
        logger.info(f"⏰ Schedule: Daily at {Config.SCHEDULE_TIME}")
        logger.info(f"🤖 Model: {Config.MODEL_NAME}")

        # Initialize scheduler
        scheduler = NewsScheduler()

        # Schedule the daily job
        scheduler.schedule_daily_news(send_daily_digest)
        scheduler.start()

        # Show next run
        next_run = scheduler.get_next_run()
        logger.info(f"📅 Next scheduled run: {next_run}")

        logger.info("🚀 Application running. Press Ctrl+C to stop.")
        logger.info("=" * 60)

        # Keep the application running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("\n⏹️ Shutting down...")
        try:
            scheduler.stop()
        except NameError:
            pass
        logger.info("Application stopped")

    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        exit(1)

    except Exception as e:
        logger.error(f"Fatal error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
