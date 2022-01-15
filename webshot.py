from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.help import module_list, file_list

@Client.on_message(filters.command("webshot", prefixes='!') & filters.me)
async def webshot(client, message):
    try:
        user_link = message.command[1]
        await message.delete()
        full_link = f"https://webshot.deam.io/{user_link}/?delay=2000"
        await client.send_document(message.chat.id, full_link, caption=f"Скриншот страницы {user_link}.")
    except:
        await message.delete()
        await client.send_message(
            message.chat.id, "<code>Something went wrong...</code>"
        )
        
module_list['Webshot'] = '!webshot'
file_list['Webshot'] = 'webshot.py'