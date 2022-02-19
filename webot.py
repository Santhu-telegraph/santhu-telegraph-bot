import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Webot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Webot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>ʜᴇʟʟᴏ.. 💝 ɴᴇɴᴜ ᴍᴇ ᴛᴇʟᴇɢʀᴀᴘʜ ʙᴏᴛ ɴɪ.. 😊

ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴘʜᴏᴛᴏs ᴏʀ ᴠɪᴅᴇᴏs ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.ᴘᴏᴡᴇʀᴇᴅ ʙʏ: @santhuvc

ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "💙ɴɪʙʙᴀ ʜᴇʟᴘ💛", callback_data="help"),
                                        InlineKeyboardButton(
                                            "🔰ɴᴇᴛᴡᴏʀᴋ🔰", url="https://t.me/santhuvc")
                                    ],[
                                      InlineKeyboardButton(
                                            "💚ɴɪʙʙᴀ sᴀɴᴛʜᴜ❤❤", url="https://t.me/santhu_music_bot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

ᴊᴜsᴛ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ʟᴇss ᴛʜᴀɴ 𝟻ᴍʙ ғɪʟᴇ sɪᴢᴇ, ɪ'ʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.

ᴊᴏɪɴ ғᴏʀ ᴜᴘᴅᴀᴛᴇs: @santhuvc</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "◁", callback_data="start"),
                                        InlineKeyboardButton(
                                            "🙄ᴀʙᴏᴜᴛ ɴɪʙʙᴀ🧐", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "💚ɴɪʙʙᴀ sᴀɴᴛʜᴜ❤💖", url="https://t.me/santhu_music_bot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>🤎ᴏᴡɴᴇʀ💘:</b> <a href="https://t.me/santhu_music_bot">Santhu </a>

<b>💝ɴᴇᴛᴡᴏʀᴋ💖:</b> <a href="https://t.me/santhuvc">Santhu vc </a>


<b>~ @santhuvc</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "◁", callback_data="help"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**https://telegra.ph{response[0]}**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**https://telegra.ph{response[0]}**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.text)
async def telegraphtext(client, message):
    msg = await message.reply_text("ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("text should be less than 5mb!") 
    else:
        await msg.edit_text(f'**https://telegra.ph{response[0]}**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Nibba bot started successfully 💘!
Join @santhuvc
"""
)

Webot.run()
