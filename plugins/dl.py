from pyrogram import Client, filters

@Client.on_message(filters.regex(r"(https?:\/\/(?:www\.)?instagram\.com\/p\/([^/?#&]+)).*"))
def dl_post(c, m):
    m.reply("Test")