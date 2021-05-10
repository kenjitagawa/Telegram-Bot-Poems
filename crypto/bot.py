from dotenv import load_dotenv
import os

from telegram.ext import Updater, CommandHandler
import logging


load_dotenv()

# Setting up the bot
updater = Updater(token=os.getenv("TOKEN"), use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(filename='bot.log', filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def start(update, context):
    message = 'Welcome to the AME Crypto Bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def get_crypto(update, context):
    message = "Here are the prices for the following crypto currencies: "
    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# updater.start_webhook(url_path=f"/{os.getenv('SECRET')}")

if __name__ == '__main__':
    updater.start_polling()