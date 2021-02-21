from pyrogram import Client

api_id = 1691381
api_hash = "a4b862a161f7a320d5524730bbf51bf2"
token = ""
bot = Client("sefl-v-02", api_id, api_hash,
             workers=4, plugins=dict(root="plugins"), bot_token=token)

bot.run()