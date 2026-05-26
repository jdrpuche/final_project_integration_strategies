# 🎵 Daily Music News - Setup Guide

## ✅ What's Been Set Up

Your project is almost ready! Here's what I've created:

```
daily_music_news/
├── main.py              # Main application (run this to start)
├── config.py            # Configuration management
├── news_fetcher.py      # NewsAPI integration
├── summarizer.py        # Langchain + OpenAI summarization
├── email_sender.py      # Gmail SMTP sender
├── scheduler.py         # APScheduler setup
├── pyproject.toml       # Dependencies (installed with UV)
├── .env                 # Your credentials (partially filled)
├── .env.example         # Template for reference
├── .venv/               # Virtual environment (ready)
├── README.md            # Full documentation
└── .gitignore          # Git configuration
```

**Installed Packages:**
- ✅ APScheduler (for cron scheduling)
- ✅ Langchain + Langchain-OpenAI (for LLM)
- ✅ Python-dotenv (for environment variables)
- ✅ Requests (for API calls)

---

## ⚠️ Action Items - Get These Credentials

### 1️⃣ NewsAPI Key (Required)
**What:** API key for fetching music news
**How to get:**
1. Go to https://newsapi.org
2. Click "Get API Key"
3. Sign up for free
4. Copy your API key from the dashboard

**Add to `.env`:**
```
NEWSAPI_KEY=your_newsapi_key_here
```

### 2️⃣ Gmail App Password (Required)
**What:** Special 16-character password for app authentication
**How to get:**
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer" (or your device)
3. Google will generate a 16-character password
4. Copy and save it (you'll only see it once)

**Add to `.env`:**
```
GMAIL_APP_PASSWORD=your_16_char_password
```

### 3️⃣ OpenAI API Key (Already Added)
✅ Your OpenAI key is already configured in `.env`

---

## 🚀 Quick Start

### Activate Virtual Environment
```bash
cd /home/esus/final_project_integration_strategies/daily_music_news
source .venv/bin/activate
```

### Update `.env` with Missing Credentials
Edit the `.env` file and fill in:
- `NEWSAPI_KEY` - from newsapi.org
- `GMAIL_APP_PASSWORD` - from Gmail settings

### Test Configuration
```bash
python config.py
```
Output should show: ✅ Configuration validated successfully!

### Run the Application
```bash
python main.py
```

You'll see:
```
⏰ Next scheduled run: 2026-05-25 08:00:00
🚀 Application running. Press Ctrl+C to stop.
```

---

## 📋 How It Works

1. **APScheduler** runs at your configured time (default: 08:00)
2. **news_fetcher.py** calls NewsAPI to get latest music news
3. **summarizer.py** uses OpenAI + Langchain to create a summary
4. **email_sender.py** sends the summary via Gmail
5. **Logs** are saved to `daily_music_news.log`

---

## 🧪 Testing

### Test Email Sending
```bash
python
>>> from email_sender import GmailSender
>>> sender = GmailSender()
>>> sender.send_music_news_digest("<h2>Test</h2>")
```

### Test News Fetching
```bash
python
>>> from news_fetcher import NewsAPIFetcher
>>> fetcher = NewsAPIFetcher()
>>> articles = fetcher.fetch_music_news(limit=5)
```

### Test Summarization
```bash
python
>>> from summarizer import NewsSummarizer
>>> summarizer = NewsSummarizer()
>>> summary = summarizer.summarize("Test articles...")
```

---

## 📝 Customization

### Change Schedule Time
Edit `.env`:
```
SCHEDULE_TIME=14:30  # 2:30 PM instead of 8:00 AM
```

### Change LLM Model
Edit `.env`:
```
MODEL_NAME=gpt-4  # Use GPT-4 instead of GPT-3.5-turbo
```

### Change News Query
Edit `config.py`, line ~20:
```python
NEWS_QUERY = "music"  # Change to "rock", "k-pop", etc.
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Gmail login fails | Ensure you used App Password (not regular password) |
| No news articles | Check NewsAPI key is valid and hasn't hit rate limit |
| OpenAI error | Verify API key has credits available |
| Scheduler won't start | Check all required env vars are set (run `python config.py`) |

---

## 📧 What the Email Looks Like

Recipients will receive a beautifully formatted HTML email with:
- 🎵 Daily Music News Digest header
- Top stories with descriptions
- Direct links to full articles
- Key music industry trends
- Formatted with purple gradient header

---

## ⏹️ Stop the Application

Press `Ctrl+C` in the terminal where the app is running.

---

## 🎯 Next Steps

1. ✏️ Get your NewsAPI key and add to `.env`
2. ✏️ Get your Gmail App Password and add to `.env`
3. 🧪 Run `python config.py` to validate
4. 🚀 Run `python main.py` to start
5. 📅 Set and forget! It runs daily at 08:00

---

**Questions?** Check the README.md or individual module docstrings!
