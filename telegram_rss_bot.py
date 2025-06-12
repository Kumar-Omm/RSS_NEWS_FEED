import logging
import asyncio
import feedparser
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN"
RSS_FEED_URL = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"  # Or use any other like https://news.google.com/rss

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_latest_news(limit=5):
    feed = feedparser.parse(RSS_FEED_URL)
    if not feed.entries:
        return ["No news found."]
    
    news_items = []
    for entry in feed.entries[:limit]:
        title = entry.title
        link = entry.link
        news_items.append(f"📰 {title}\n🔗 {link}")
    return news_items

async def send_news(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    news_items = fetch_latest_news()
    for news in news_items:
        await context.bot.send_message(chat_id=chat_id, text=news)

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news_items = fetch_latest_news()
    for news in news_items:
        await update.message.reply_text(news)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /news to get the latest news.")

async def setup_commands(app):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("news", "Get latest news"),
    ]
    await app.bot.set_my_commands(commands)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))

    # Set Telegram command list
    app.job_queue.run_once(lambda ctx: asyncio.create_task(setup_commands(app)), when=1)

    # Schedule hourly news
    app.job_queue.run_repeating(send_news, interval=60, first=10)

    logger.info("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
# Ensure to replace YOUR_BOT_TOKEN_HERE with your actual Telegram bot token.
