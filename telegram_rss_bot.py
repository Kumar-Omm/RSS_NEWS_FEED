import logging
import feedparser
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

TELEGRAM_BOT_TOKEN = 'BOT_TOKEN_HERE'
RSS_FEED_URL = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
CHAT_ID = 'YOUR_CHAT_ID_HERE'  

sent_links = set()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_rss():
    feed = feedparser.parse(RSS_FEED_URL)
    news_items = []

    for entry in feed.entries:
        if entry.link not in sent_links:
            news_items.append(f"📰 <b>{entry.title}</b>\n{entry.link}")
            sent_links.add(entry.link)
    
    return news_items

def send_news(update: Update, context: CallbackContext):
    news_items = fetch_rss()
    if not news_items:
        update.message.reply_text("No new news right now.")
        return
    for news in news_items:
        context.bot.send_message(chat_id=update.effective_chat.id, text=news, parse_mode='HTML')

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('news', send_news))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
