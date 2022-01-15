from pyrogram import Client, filters
from plugins.help import module_list
import os

@Client.on_message(filters.command('loadmod', prefixes='!'))
async def loadmod(client, message):
    try:
        params = message.text.replace('!loadmod', '')
        params = params.split()
        link = params[0]
        os.system(f'wget -P plugins/ {link}')
        await message.edit("**Модуль успешно загружен.**")
    except:
        await message.edit("**Произошла ошибка!**")
    
module_list['Loadmod'] = '!loadmod [ссылка на модуль]'