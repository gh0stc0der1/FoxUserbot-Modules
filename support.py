from pyrogram import Client, filters
from plugins.help import module_list, file_list

@Client.on_message(filters.command('support', prefixes='!'))
async def support(client, message):
    await message.delete()
    await client.send_photo(
    chat_id=message.chat.id,
    photo="logo.jpg",
    caption="""**FOX USERBOT**
```По всем вопросам и предложениям обращаться к``` @foxuserbot_000."""
)

module_list['Support'] = '!support'
file_list['Support'] = 'support.py'