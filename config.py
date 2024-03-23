from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

# استدعاء المتغيرات البيئية
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
SESSION = os.environ.get("TERMUX")
TOKEN = os.environ.get("TOKEN")

# تأكد من وجود القيم المطلوبة
if not all([APP_ID, APP_HASH, BOT_USERNAME, SESSION, TOKEN]):
    raise ValueError("يرجى تعيين جميع المتغيرات البيئية APP_ID، APP_HASH، BOT_USERNAME، TERMUX، و TOKEN")

# إنشاء جلسة للتفاعل مع التطبيق
sython = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)

# تأكد من تعيين المتغيرات البيئية بشكل صحيح
if not all([APP_ID, APP_HASH, TOKEN]):
    raise ValueError("يرجى تعيين جميع المتغيرات البيئية APP_ID، APP_HASH، و TOKEN")

# بدء التفاعل مع التطبيق
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=TOKEN)
