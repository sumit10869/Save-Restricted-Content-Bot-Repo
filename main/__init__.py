#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()
MDB = "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn"
API_ID = "21513517" #config("API_ID", default=None, cast=int)
API_HASH = "838d3451485b95722878921877f12066" #config("API_HASH", default=None)
BOT_TOKEN = "6839630607:AAERKjFuMly87MJH1-dxzY-WJCMlCv34iTw" #config("BOT_TOKEN", default=None)
SESSION = "BQFxJpUADRb6nGpf6RWbfp2dsl6jQHaKVjYTP5-BZwNh707mM5BGBad8SXW5_mHLt20OISKWW-0h6kPi6pB9uNVsOZP_dot0TI6WygZsUOuDnuFFavNaptGOkSjQLKd3x4cCU5YoljEChwILuIjMOnw8obVHJA1Q8ZvUH1TgyS8uwl-aUQbmjsNNuuPFVD1BECfXw0bs4w14a6yhNLNGmFBII1E_9N40JyxKr8bQU4O_wOx-_amaoKtmLNQqLJBOcAXG9MPn9DqiJuvHkFyebCsROM2hoT2jtPReruXcqwwNhoccUtKfmrU9wS7DuL3UNK-MvVIc2yVCnb3ThXcEh1BUw4B00AAAAAGhhwirAA" #config("SESSION", default=None)
FORCESUB = "official_satyam01" #config("FORCESUB", default=None)
AUTH = "7004948651" #config("AUTH", default=None)
MONGODB = "mongodb+srv://satyamyt10869:Sumit10869@cluster0.0ojjo0p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #config("MONGODB", default=MDB)
OWN = 7004948651 # edit this
GROUP = -1002238804331 # edit this
OWNER_ID = int(config("OWNER_ID", default=OWN))
LOG_GROUP = int(config("LOG_GROUP", default=GROUP))

SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
