import dotenv
import os
import logging
from rpd import BotApp

logging.basicConfig(level=logging.DEBUG)  # i just do this since i develop the lib and love to see errors ofc!
dotenv.load_dotenv()

bot = BotApp(token=os.getenv("token"), intents=32767)

async def add():
    await bot.change_presence("h", 0)

bot.state.loop.create_task(add())
bot.run()