#!/usr/bin/env python3
"""Interactive script to configure credentials."""

import os
import sys
from pathlib import Path

def update_env(key: str, value: str):
    """Update or add a key-value pair in .env file."""
    env_path = Path(__file__).parent / ".env"
    
    if not env_path.exists():
        print(f"❌ .env file not found at {env_path}")
        return False
    
    with open(env_path, 'r') as f:
        lines = f.readlines()
    
    # Find and replace or add the key
    found = False
    updated_lines = []
    
    for line in lines:
        if line.startswith(f"{key}="):
            updated_lines.append(f"{key}={value}\n")
            found = True
        else:
            updated_lines.append(line)
    
    # If not found, add it at the end
    if not found:
        updated_lines.append(f"\n{key}={value}\n")
    
    with open(env_path, 'w') as f:
        f.writelines(updated_lines)
    
    return True

def main():
    """Main interactive configuration."""
    print("\n" + "="*60)
    print("🎵 Daily Music News - Configuration Setup")
    print("="*60 + "\n")
    
    # NewsAPI Key
    print("📰 STEP 1: NewsAPI Configuration")
    print("-" * 60)
    print("1. Go to https://newsapi.org")
    print("2. Sign up (free tier available)")
    print("3. Copy your API key from the dashboard\n")
    
    newsapi_key = input("Paste your NewsAPI key (or press Enter to skip): ").strip()
    if newsapi_key:
        if update_env("NEWSAPI_KEY", newsapi_key):
            print("✅ NewsAPI key saved!\n")
        else:
            print("❌ Failed to save NewsAPI key\n")
    else:
        print("⏭️  Skipped (you can add this later)\n")
    
    # Gmail App Password
    print("📧 STEP 2: Gmail App Password")
    print("-" * 60)
    print("1. Go to https://myaccount.google.com/apppasswords")
    print("2. Select 'Mail' and 'Windows Computer' (or your device)")
    print("3. Google will generate a 16-character password")
    print("4. Copy the password (you'll only see it once!)\n")
    
    gmail_pwd = input("Paste your Gmail App Password (or press Enter to skip): ").strip()
    if gmail_pwd:
        if update_env("GMAIL_APP_PASSWORD", gmail_pwd):
            print("✅ Gmail App Password saved!\n")
        else:
            print("❌ Failed to save Gmail App Password\n")
    else:
        print("⏭️  Skipped (you can add this later)\n")
    
    # Optional: Change schedule time
    print("⏰ STEP 3: Schedule Time (Optional)")
    print("-" * 60)
    print("Current schedule time: 08:00 (8:00 AM)")
    
    change_time = input("Change schedule time? (Enter HH:MM or press Enter to keep 08:00): ").strip()
    if change_time and ":" in change_time:
        if update_env("SCHEDULE_TIME", change_time):
            print(f"✅ Schedule time changed to {change_time}!\n")
    else:
        print("✅ Schedule time remains 08:00\n")
    
    # Summary
    print("="*60)
    print("✅ Configuration Complete!")
    print("="*60 + "\n")
    
    print("To verify and start your application, run:")
    print("  python config.py     (verify configuration)")
    print("  python main.py       (start the application)\n")
    
    print("Your daily music news digest will be sent daily! 🎵\n")

if __name__ == "__main__":
    main()
