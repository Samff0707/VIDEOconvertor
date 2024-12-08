from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("29285954", default=None, cast=int)
API_HASH = config("ee47f0d64723ee82fe3968ab09efbe3c", default=None)
BOT_TOKEN = config("7634604356:AAFSSHCbaV1_BcAGQWNGuQQxKdC2e_f3awk", default=None)
BOT_UN = config("BOT_UN", default=None)
AUTH_USERS = config("AUTH_USERS", default=None, cast=int)
LOG_CHANNEL = config("1002299313089", default=None)
LOG_ID = config("1002302087024", default=None)
FORCESUB = config("FORCESUB", default=None)
FORCESUB_UN = config("FORCESUB_UN", default=None)
ACCESS_CHANNEL = config("1002330768286", default=None)
MONGODB_URI = config("mongodb+srv://surajsam50:WCQbVAjfFctbSW7j@cluster0.pwkld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", default=None)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
