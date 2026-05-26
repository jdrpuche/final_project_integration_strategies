# 📧 On-Demand Email Sending

Your Daily Music News app now supports sending emails **whenever you want**, not just on schedule!

## 🚀 Two Ways to Send

### Option 1: Quick Send (Recommended)
```bash
python send_now.py
```

This is the simplest way. Just run it and it sends immediately!

**Output:**
```
🎵 Sending Music News Digest (On-Demand)
📰 Fetching music news...
🤖 Generating AI summary...
📧 Sending email...
✅ Music news digest sent successfully!
```

### Option 2: Using Main App with Flag
```bash
python main.py --send-now
```

Or use the short flag:
```bash
python main.py -s
```

This sends the digest immediately using the main application.

## 📋 Usage Examples

### Send digest now and check email
```bash
source .venv/bin/activate
python send_now.py
# Check inbox immediately!
```

### Test the full pipeline
```bash
python send_now.py
# Verify it works before setting up the scheduler
```

### Then run the scheduler
```bash
python main.py
# Will send daily at 08:00 and accept --send-now flag anytime
```

## ⚙️ How It Works

Both methods:
1. ✅ Fetch latest music news
2. ✅ Generate AI summary with OpenAI
3. ✅ Create beautiful HTML email
4. ✅ Send via Gmail
5. ✅ Log the results

Takes about 15-20 seconds total.

## 🎯 Common Workflows

### Development/Testing
```bash
# Quickly test your setup
python send_now.py

# Check email formatting
# Adjust settings if needed
```

### Production
```bash
# Run the scheduler for daily emails
python main.py

# Anytime you want an extra digest
python send_now.py
```

### Troubleshooting
```bash
# Send now and see detailed logs
python send_now.py

# Check the full log file
tail -f daily_music_news.log
```

## 🔄 Run Both (Scheduler + On-Demand)

You can run the scheduler in one terminal and send on-demand emails in another:

**Terminal 1** (Scheduler):
```bash
source .venv/bin/activate
python main.py
```

**Terminal 2** (Send on-demand):
```bash
source .venv/bin/activate
python send_now.py
```

Both work independently!

## 💡 Tips

- **Quick test:** `python send_now.py` before setting up the scheduler
- **Multiple sends:** Send as many times as you want, no limits
- **No scheduling:** Use `send_now.py` if you don't want automatic daily emails
- **Manual + Auto:** Run both `main.py` and `send_now.py` for flexibility

## ✨ That's It!

Send music news digests **whenever you want**! 🎵
