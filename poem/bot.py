from dotenv import load_dotenv
import os

import telegram
from telegram.ext import Updater, CommandHandler
import logging

from poem import get_poem


load_dotenv()

# Setting up the bot
updater = Updater(token=os.getenv("TOKEN"), use_context=True)

dispatcher = updater.dispatcher


# 
logging.basicConfig(filename='bot.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def start(update, context):
    message = 'Welcome to the Poem Bot!'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def send_poem(update, context):
    poem = get_poem()

    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text=poem)

    except telegram.error.BadRequest:
        poem = get_poem()
        context.bot.send_message(chat_id=update.effective_chat.id, text=poem)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

poem_handler = CommandHandler('poem', send_poem)
dispatcher.add_handler(poem_handler)

# updater.start_webhook(url_path=f"/{os.getenv('SECRET')}")

if __name__ == '__main__':
    updater.start_polling()