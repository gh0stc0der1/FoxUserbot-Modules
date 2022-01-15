from pyrogram import Client, filters
from plugins.help import module_list
import os

@Client.on_message(filters.command('unloadmod', prefixes='!'))
async def unloadmod(client, message):
    try:
        module_name = message.text.replace('!unloadmod', '')
        params = module_name.split()
        module_name = params[0]
        del module_list[module_name]
        file = file_list[module_name]
        os.system(f'rm plugins/{file}')
        await message.edit(f"**Модуль** ```{module_name}``` **успешно деинсталлирован.**")
    except:
        await message.edit("**Произошла ошибка.**")
 
module_list['Unloadmod'] = '!unloadmod [название модуля]'