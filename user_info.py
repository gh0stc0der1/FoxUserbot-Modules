import asyncio
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from plugins.help import module_list, file_list

@Client.on_message(filters.command("user_info", prefixes='!') & filters.me)
async def get_user_inf(client, message):
    if len(message.text.split()) >= 2:
        try:
            user = await client.get_users(message.text.split()[1])
            user = user.id
        except:
            try:
                user = message.reply_to_message.from_user.id
            except:
                user = message.from_user.id
    else:
        try:
            user = message.reply_to_message.from_user.id
        except:
            user = message.from_user.id
    user_info = await client.send(
        functions.users.GetFullUser(id=await client.resolve_peer(user))
    )
    if user_info.users[0].username is None:
        username = "None"
    else:
        username = f"@{user_info.users[0].username}"
    about = "None" if user_info.full_user.about is None else user_info.full_user.about
    user_info = f"""|=<b>Username: {username}
|-Id: <code>{user_info.users[0].id}</code>
|-Bot: <code>{user_info.users[0].bot}</code>
|-Scam: <code>{user_info.users[0].scam}</code>
|-Name: <code>{user_info.users[0].first_name}</code>
|-Deleted: <code>{user_info.users[0].deleted}</code>
|-BIO: <code>{about}</code>
</b>"""
    await message.edit(user_info)


@Client.on_message(filters.command("user_info_full", prefixes='!') & filters.me)
async def get_full_user_inf(client: Client, message: Message):
    await message.edit("<code>Receiving the information...</code>")
    if len(message.text.split()) >= 2:
        try:
            user = await client.get_users(message.text.split()[1])
            user = user.id
        except:
            try:
                user = message.reply_to_message.from_user.id
            except:
                user = message.from_user.id
    else:
        try:
            user = message.reply_to_message.from_user.id
        except:
            user = message.from_user.id
    try:
        msg = await client.send_message("@creationdatebot", f"/id {user}")
        await asyncio.sleep(1)
        date_dict = await client.get_history("@creationdatebot")
        date_dict = date_dict[0].text
        await client.send(
            functions.messages.DeleteHistory(
                peer=await client.resolve_peer(747653812), max_id=msg.chat.id
            )
        )
        user_info = await client.send(
            functions.users.GetFullUser(id=await client.resolve_peer(user))
        )
        if user_info.users[0].username is None:
            username = "None"
        else:
            username = f"@{user_info.users[0].username}"
        about = "None" if user_info.full_user.about is None else user_info.full_user.about
        user_info = f"""|=<b>Username: {username}
|-Id: <code>{user_info.users[0].id}</code>
|-Account creation date: <code>{date_dict}</code>
|-Bot: <code>{user_info.users[0].bot}</code>
|-Scam: <code>{user_info.users[0].scam}</code>
|-Name: <code>{user_info.users[0].first_name}</code>
|-Deleted: <code>{user_info.users[0].deleted}</code>
|-BIO: <code>{about}</code>
|-Contact: <code>{user_info.users[0].contact}</code>
|-Can pin message: <code>{user_info.full_user.can_pin_message}</code>
|-Mutual contact: <code>{user_info.users[0].mutual_contact}</code>
|-Access hash: <code>{user_info.users[0].access_hash}</code>
|-Restricted: <code>{user_info.users[0].restricted}</code>
|-Verified: <code>{user_info.users[0].verified}</code>
|-Phone calls available: <code>{user_info.full_user.phone_calls_available}</code>
|-Phone calls private: <code>{user_info.full_user.phone_calls_private}</code>
|-Blocked: <code>{user_info.full_user.blocked}</code></b>"""
        await message.edit(user_info)
    except:
        await msg.edit("An error has occurred...")
        
module_list['Userinfo'] = '!user_info | !user_info_full'
file_list['Userinfo'] = 'user_info.py'