#!/bin/bash
# Quick Start Script for Daily Music News
# Save this and run: bash quickstart.sh

cd /home/esus/final_project_integration_strategies/daily_music_news

echo "🎵 Daily Music News - Quick Start"
echo "=================================="
echo ""

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    exit 1
fi

# Activate venv
echo "✅ Activating virtual environment..."
source .venv/bin/activate

echo ""
echo "📋 Next Steps:"
echo "1. Get NewsAPI key: https://newsapi.org"
echo "2. Get Gmail app password: https://myaccount.google.com/apppasswords"
echo "3. Run: python setup_credentials.py"
echo "4. Run: python main.py"
echo ""

# Show current status
echo "📊 Current Status:"
python3 << EOF
import os
from pathlib import Path
from dotenv import load_dotenv

env_file = Path(".env")
load_dotenv(".env")

newsapi = os.getenv("NEWSAPI_KEY", "").startswith("GET_")
gmail_pwd = os.getenv("GMAIL_APP_PASSWORD", "").startswith("GET_")
openai = "sk-" in os.getenv("OPENAI_API_KEY", "")

print(f"✅ Python Virtual Environment: Ready")
print(f"{'⏳' if newsapi else '✅'} NewsAPI Key: {'NEEDED' if newsapi else 'Configured'}")
print(f"{'⏳' if gmail_pwd else '✅'} Gmail App Password: {'NEEDED' if gmail_pwd else 'Configured'}")
print(f"{'⏳' if not openai else '✅'} OpenAI API Key: {'NEEDED' if not openai else 'Configured'}")
print(f"✅ Email Recipient: {os.getenv('RECIPIENT_EMAIL', 'Not set')}")
print(f"✅ Schedule Time: {os.getenv('SCHEDULE_TIME', 'Not set')}")
EOF

echo ""
echo "🚀 Ready to run! Use: python main.py"
