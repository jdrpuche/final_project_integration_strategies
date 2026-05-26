"""Configuration management for daily music news application."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
ENV_PATH = Path(__file__).parent / ".env"
load_dotenv(ENV_PATH)


class Config:
    """Application configuration."""

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

    # NewsAPI Configuration
    NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
    NEWSAPI_BASE_URL = os.getenv("NEWSAPI_BASE_URL", "https://newsapi.org/v2")
    NEWS_QUERY = "music"
    NEWS_LANGUAGE = "en"
    NEWS_SORT_BY = "publishedAt"

    # Gmail Configuration
    GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
    GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "jdrpuche@gmail.com")

    # Schedule Configuration
    SCHEDULE_TIME = os.getenv("SCHEDULE_TIME", "08:00")

    @staticmethod
    def validate():
        """Validate that all required config values are set."""
        required = [
            "OPENAI_API_KEY",
            "NEWSAPI_KEY",
            "GMAIL_ADDRESS",
            "GMAIL_APP_PASSWORD",
            "RECIPIENT_EMAIL",
        ]

        missing = [key for key in required if not getattr(Config, key)]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}. "
                "Please check your .env file."
            )


if __name__ == "__main__":
    Config.validate()
    print("✅ Configuration validated successfully!")
    print(f"📧 Email recipient: {Config.RECIPIENT_EMAIL}")
    print(f"⏰ Schedule time: {Config.SCHEDULE_TIME}")
    print(f"🤖 Model: {Config.MODEL_NAME}")
