from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
SESSION = os.environ.get("TERMUX")
TOKEN = os.environ.get("TOKEN")

# تأكد من أن البيانات التي تم تمريرها إلى TelegramClient صحيحة وموجودة
if APP_ID and APP_HASH and SESSION:
    sython = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
else:
    print("تأكد من تعيين متغيرات البيئة APP_ID، APP_HASH، وSESSION بشكل صحيح.")

# تأكد من تعيين المتغيرات البيئية بشكل صحيح
if APP_ID and APP_HASH and TOKEN:
    bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=TOKEN)
else:
    print("تأكد من تعيين متغيرات البيئة APP_ID، APP_HASH، وTOKEN بشكل صحيح.")

# احذف هذا السطر إذا كنت قد بدأت البوت بالفعل
# bot.start()
