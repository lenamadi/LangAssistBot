from telethon import TelegramClient , events
from config import api_id , api_hash
client = TelegramClient('bot_session'api_id=,api_id=)

@client.on(events.NewMessage(pattern=r'/start'))
async def start(event):
    await client.send_message(entity=event.chat_id , message="halloooo")


client.start(bot_token="")
client.run_until_disconnected()