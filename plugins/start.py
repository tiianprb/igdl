from pyrogram import Client, filters

START_MESSAGE = "Welcome"

@Client.on_message(filters.command("start",'/'))
def start_messgae(c, m):
    m.reply_text(START_MESSAGE)
    