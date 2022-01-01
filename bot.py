from pyrogram import Client, filters

api_id = 14448837
api_hash = "06b79ae95202e27931b152dba1903459"
token = "5099807719:AAEdd2nm4c0qM5ksZAQjo3XaqYNq3Hmfj50"
bot = Client("igdl", api_id, api_hash,
             workers=4, plugins=dict(root="plugins"), bot_token=token)


bot.set_parse_mode('md')


bot.run()
