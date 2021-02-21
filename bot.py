from pyrogram import Client, filters

api_id = 1691381
api_hash = "a4b862a161f7a320d5524730bbf51bf2"
token = "1622516881:AAFSmoSck8T49NRGz6GqsknTJfYFujYtagg"
bot = Client("igdl", api_id, api_hash,
             workers=4, plugins=dict(root="plugins"), bot_token=token)


bot.set_parse_mode('md')


bot.run()