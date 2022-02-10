import discord
import os
import dotenv

dotenv.load_dotenv()

client = discord.Client()

client.run(os.getenv("token"))