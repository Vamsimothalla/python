#!/usr/bin/env python
api_id = '1293341'
api_hash = '951efa9687bd986c2947a4ac2a6b6b0c'

bot = TelegramClient('xxx', api_id, api_hash).start(bot_token='1184021844:AAG2Zhx-6GSRHKYgQWrbIWSAi2zOFN5Pdo8')
@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
   await event.reply('Howdy, how are you doing?')

@bot.on(events.NewMessage)
async def echo_all(event):
   await event.reply(event.text)

bot.run_until_disconnected()
