import asyncio
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from plugins.help import module_list, file_list

@Client.on_message(
    filters.command(["scr", "screenshot"], prefixes='!') & filters.private & filters.me
)
async def screenshot(client: Client, message: Message):
    quantity = int(message.command[1])
    await message.delete()
    for _ in range(quantity):
        await asyncio.sleep(0.1)
        await client.send(
            functions.messages.SendScreenshotNotification(
                peer=await client.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=client.rnd_id(),
            )
        )
        
module_list['Screenshot'] = '!scr | !screenshot'
file_list['Screenshot'] = 'screenshot.py'
