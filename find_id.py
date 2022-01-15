from pyrogram import Client, filters
from plugins.help import module_list, file_list
import asyncio

@Client.on_message(filters.command('find_id', prefixes='!') & filters.me)
async def find_id(client, message):
  await message.edit(f'**Айди этого чата:** ```{message.chat.id}```')
  
module_list['FindIDThisChat'] = '!fing_id'
file_list['FindIDThisChat'] = 'find_id.py'
