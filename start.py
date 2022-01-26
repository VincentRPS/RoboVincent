import logging
import os

import dotenv
from rpd import BotApp

logging.basicConfig(level=logging.DEBUG)  # i just do this since i develop the lib and love to see errors and fuck ups!
dotenv.load_dotenv()

bot = BotApp(token=os.getenv("token"), intents=32767)

if bot.state._ready.is_set() is True:
    print("Bot is ready!")

bot.run()