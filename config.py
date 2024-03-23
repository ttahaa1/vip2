# في ملف sython.py

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
import asyncio

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

# تعريف الحدث
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
    await event.edit("حسنا، تأكد من أنك مشترك في قنوات الاشتراك الإجباري لتجنب الأخطاء")
    channel_entity = await sython.get_entity(BOT_USERNAME)
    await sython.send_message('@EEObot', 'جاري التجميع بواسطة | 𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗗𝗧𝗛𝗢𝗡')
    await asyncio.sleep(5)
    msg0 = await sython.get_messages('@EEObot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(5)
    msg1 = await sython.get_messages('@EEObot', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(5)
        list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython(ImportChatInviteRequest(bott))
            msg2 = await sython.get_messages('@EEObot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
        except:
            await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
            break
    await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")

# بدء تفاعل العميل
sython.start()
sython.run_until_disconnected()
