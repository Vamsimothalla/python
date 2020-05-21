#!/usr/bin/env python
api_id = ''
api_hash = ''

bot = TelegramClient('xxx', api_id, api_hash).start(bot_token='1184021844:AAG2Zhx-6GSRHKYgQWrbIWSAi2zOFN5Pdo8')
@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
   await event.reply('Howdy, how are you doing?')

@bot.on(events.NewMessage)
async def echo_all(event):
   await event.reply(event.text)

bot.run_until_disconnected()
