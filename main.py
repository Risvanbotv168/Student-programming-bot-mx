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
    await message.reply_text("Hello..! My name is mallu filter bot , i can provide movies ,  just  add  me to  group an    And one more thing, I'm a filter bot😇")


@MALLU_FILTER.on_message(filters.command("help"))
async def help_cmd(client‚message):
    await message.reply_text("Please personal message @Riwan_x")

@MALLU_FILTER.on_message(filters.command("settings"))
async def settings_cmd(client‚message):
    await message.reply_text("I'm not connected to any groups!")

@MALLU_FILTER.on_message(filters.command("connect"))
async def connect_cmd(client‚message):
    await message.reply_text("Enter in correct format!

/connect groupid

Get your Group id by adding this bot to your group and use  /id

@MALLU_FILTER.on_message(filters.command("filter"))
async def filter_cmd(client‚message):
    await message.reply_text("I'm not connected to any groups!")



print("Bot Started")

MALLU_FILTER.run()
