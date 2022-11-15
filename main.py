from pyrogram import Client‚ filters

API_ID = "10874827"
API_HASH = "b31a3277eaa54329f0c183ab769319be"
BOT_TOKEN = "5682753013:AAGNKu2DCp2w8OjpUapmDwxcKbZzvVbR1MI"

MALLU_FILTER = Client(
   name="MALLU_FILTER"
   api_id=API_ID‚
   api_hash=API-HASH‚
   bot_token=BOT_TOKEN‚
)

@MALLU_FILTER.on_message(filters.command("start"))
async def start_cmd(client‚message):
    print("START Command")


@MALLU_FILTER.on_message(filters.command("help"))
async def help_cmd(client‚message):
    print("HELP Command")

@MALLU_FILTER.on_message(filters.command("settings"))
async def settings_cmd(client‚message):
    print("SETTINGS Command")


print("Bot Started")

MALLU_FILTER.run()
