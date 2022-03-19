import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
from handlers import start, unknown, echo, hello, draco_price, hidra_price


load_dotenv('.env')
updater = Updater(os.environ['TELEGRAM_TOKEN'])


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('draco', draco_price))
updater.dispatcher.add_handler(CommandHandler('hidra', hidra_price))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()
