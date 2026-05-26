# 🎵 Daily Music News - Getting Started

## Welcome! 

Your Daily Music News application has been successfully set up. This file guides you through the final steps.

---

## 🎯 What You Have

A fully functional Python application that:
- ✅ Runs daily at 08:00 (customizable)
- ✅ Fetches music news from NewsAPI.org
- ✅ Summarizes using OpenAI + Langchain
- ✅ Sends beautiful email digests to your inbox
- ✅ Uses APScheduler for reliable cron scheduling

---

## 📋 3-Step Completion

### ✅ Step 1: Already Done for You
- Python virtual environment created with UV
- All dependencies installed (APScheduler, Langchain, etc.)
- Project structure and configuration system ready
- Your OpenAI API key configured

### ⏳ Step 2: Get Two API Keys (5 minutes)

#### Get NewsAPI Key
1. Visit https://newsapi.org
2. Click "Get API Key"
3. Sign up (free, takes 1 minute)
4. Copy your API key
5. Run this to add it:
   ```bash
   cd /home/esus/final_project_integration_strategies/daily_music_news
   source .venv/bin/activate
   python setup_credentials.py
   ```

#### Get Gmail App Password
1. Visit https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer"
3. Google generates a 16-character password
4. Copy it
5. Enter it when prompted by `setup_credentials.py`

### ✅ Step 3: Run It!
```bash
cd /home/esus/final_project_integration_strategies/daily_music_news
source .venv/bin/activate
python main.py
```

You should see:
```
60 seconds of logs...
📅 Next scheduled run: 2026-05-25 08:00:00
🚀 Application running. Press Ctrl+C to stop.
```

---

## 📚 Project Files

| File | Purpose |
|------|---------|
| **main.py** | Application entry point (run this) |
| **news_fetcher.py** | Fetches music news from NewsAPI |
| **summarizer.py** | Summarizes using Langchain + OpenAI |
| **email_sender.py** | Sends emails via Gmail SMTP |
| **scheduler.py** | Sets up APScheduler for daily runs |
| **config.py** | Configuration and validation |
| **setup_credentials.py** | Helper to add your API keys |
| **.env** | Your credentials (git-ignored for safety) |
| **pyproject.toml** | Python dependencies |
| **README.md** | Full documentation |

---

## 🚀 Run the App

### Option 1: Interactive Setup
```bash
cd /home/esus/final_project_integration_strategies/daily_music_news
source .venv/bin/activate
python setup_credentials.py
python main.py
```

### Option 2: Manual .env Edit
```bash
cd /home/esus/final_project_integration_strategies/daily_music_news
nano .env  # Or use VS Code to edit
# Add your NewsAPI key and Gmail app password
source .venv/bin/activate
python main.py
```

---

## 📧 What Happens

At **08:00 every day**:
1. APScheduler triggers the job
2. NewsAPI fetches the latest music news
3. Langchain + OpenAI generates a summary
4. Email is sent to jdrpuche@gmail.com

The email includes:
- 🎨 Beautiful HTML formatting
- 📰 Top music stories
- 🤖 AI-generated insights
- 🔗 Direct links to full articles

---

## 🧪 Test It

### Test Configuration
```bash
python config.py
```
Should output:
```
✅ Configuration validated successfully!
📧 Email recipient: jdrpuche@gmail.com
⏰ Schedule time: 08:00
🤖 Model: gpt-3.5-turbo
```

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
>>> print(f"Found {len(articles)} articles")
```

---

## ⚙️ Customization

### Change Time
Edit `.env`:
```
SCHEDULE_TIME=18:30  # Change from 08:00 to 6:30 PM
```

### Change News Topic
Edit `config.py` line 12:
```python
NEWS_QUERY = "rock"  # or "k-pop", "classical", etc.
```

### Use Better Model
Edit `.env`:
```
MODEL_NAME=gpt-4  # Better summaries (costs more)
```

---

## 📊 How It Works

```
Your Computer
    ↓
.venv/bin/python (Python 3.13)
    ↓
APScheduler (runs daily at 08:00)
    ↓
news_fetcher.py → calls → NewsAPI.org (gets music news)
    ↓
summarizer.py → calls → OpenAI API (generates summary)
    ↓
email_sender.py → connects to → Gmail SMTP (sends email)
    ↓
jdrpuche@gmail.com receives beautiful digest
    ↓
Repeat tomorrow at 08:00
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Gmail won't authenticate | Use App Password (not Gmail password) |
| No news fetched | Check NewsAPI key validity, check rate limits |
| OpenAI errors | Verify API key, check account credits |
| Scheduler not running | Run `python config.py` to check all settings |
| Port already in use | Change `SCHEDULE_TIME` to avoid conflicts |

---

## 📝 Logs

Application logs are saved to `daily_music_news.log`:
```bash
tail -f daily_music_news.log  # Follow logs in real-time
grep ERROR daily_music_news.log  # See errors only
```

---

## 🛑 Stop the Application

Press `Ctrl+C` in the terminal where `main.py` is running.

---

## ✨ That's It!

Your daily music news application is ready. Just:
1. Get your API keys (newsapi.org + Gmail app password)
2. Run `python setup_credentials.py` to add them
3. Run `python main.py` to start
4. Enjoy daily music news summaries! 🎵

---

## 📞 Quick Reference

```bash
# Activate environment
source .venv/bin/activate

# Add credentials interactively
python setup_credentials.py

# Validate configuration
python config.py

# Start the app
python main.py

# View logs
tail -f daily_music_news.log

# Edit configuration
nano .env  # or use VS Code
```

---

**Happy listening! 🎶**
