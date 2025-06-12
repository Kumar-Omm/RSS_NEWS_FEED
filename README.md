# 📰 Telegram News Bot

This Telegram bot fetches and sends news updates from an RSS feed to users or groups on a timed interval. Users can also manually request the latest news via a command.

## ✨ Features

- Fetches news from a configured RSS feed (e.g., BBC, Hacker News, etc.)
- Automatically sends news every hour (configurable)
- Allows manual fetching using `/news` command
- Can be added to groups or used privately
- Supports command hinting (BotFather commands)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/telegram-news-bot.git
cd telegram-news-bot
```

### 2. Make A Bot
🤖 Create and Configure Your Bot on BotFather

Open Telegram and search for @BotFather

Run /start

Use /newbot to create a new bot

Choose a name and username for your bot

Copy the Bot Token (e.g., 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11)

Paste this token into your code:

    ```bash
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"


### 3. Install Requirements

```bash
pip install -r requirements.txt
```
### 4. Run The Script

```bash
python telegram_rss_bot.py
```



