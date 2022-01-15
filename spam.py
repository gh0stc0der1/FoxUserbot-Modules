from pyrogram import Client, filters
from plugins.help import module_list, file_list
import asyncio

@Client.on_message(filters.command('spam', prefixes='!') & filters.me)
async def spam(client, message):
    spam_params = message.text.replace('!spam', '')
    spam_params = spam_params.split()
    count = spam_params[0]
    text = spam_params[1:]
    text = ' '.join(text)
    await message.edit(f"""**Спам запущен!
Количество сообщений: {count}. 
Текст спама: {text}.**""")
    for i in range(int(count)):
        await message.reply(text)
    
module_list['Spam'] = '!spam [количество сообщений] [текст]'
file_list['Spam'] = 'spam.py'