# Daily Music News Summarizer

A Python application that sends daily music news summaries to your email using APScheduler and Langchain/OpenAI.

## Features

- ✉️ Sends daily email summaries of music news
- 🎵 Fetches news from NewsAPI.org
- 🤖 Uses OpenAI GPT to summarize and format news
- ⏰ Runs on a daily schedule using APScheduler
- 📧 Gmail integration with app passwords
- 🔐 Secure credential management via .env

## Prerequisites

- Python 3.9+
- [UV package manager](https://github.com/astral-sh/uv)
- API Keys:
  - OpenAI API key (from [platform.openai.com](https://platform.openai.com))
  - NewsAPI key (free tier available at [newsapi.org](https://newsapi.org))
  - Gmail App Password (generate at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords))

## Setup

### 1. Clone and Navigate to Project
```bash
cd daily_music_news
```

### 2. Create Virtual Environment with UV
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
uv pip install -e .
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
- `OPENAI_API_KEY`: Your OpenAI API key
- `NEWSAPI_KEY`: Your NewsAPI key
- `GMAIL_ADDRESS`: Your Gmail address (sender)
- `GMAIL_APP_PASSWORD`: Your 16-character Gmail app password
- `RECIPIENT_EMAIL`: Email to receive summaries
- `SCHEDULE_TIME`: Time to send (24-hour format, e.g., "08:00")

### 5. Run the Application
```bash
python main.py
```

The application will:
1. Start the scheduler
2. Wait for the scheduled time each day
3. Fetch music news from NewsAPI
4. Generate a summary using OpenAI
5. Send the email via Gmail
6. Log all activities

## Project Structure

```
daily_music_news/
├── main.py                 # Application entry point
├── config.py              # Configuration management
├── news_fetcher.py        # NewsAPI integration
├── summarizer.py          # Langchain/OpenAI integration
├── email_sender.py        # Gmail sending logic
├── scheduler.py           # APScheduler setup
├── .env                   # Credentials (git-ignored)
├── .env.example           # Example configuration
├── pyproject.toml         # Project dependencies
└── README.md              # This file
```

## Troubleshooting

- **Gmail authentication fails**: Ensure you generated an App Password (not your regular Gmail password) at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
- **No news found**: Check that `NEWSAPI_KEY` is valid and has remaining requests
- **OpenAI errors**: Verify your API key has credits and is not expired
