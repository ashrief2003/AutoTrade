#discord interface to use for the bot (STILL MAJORLY UNDER DEVELOPMENT)
#still leaves alot to be desired

import discord
from discord.ext import commands
from imaging import *
from autotrade import *
import os
from test import *


TOKEN = "DISCORD_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def generate_random_lines_image(path):
    width, height = 800, 600
    image = np.zeros((height, width, 3), dtype=np.uint8)

    num_lines = random.randint(50, 150)

    for _ in range(num_lines):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)

        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

        thickness = random.randint(1, 5)
        cv2.line(image, (x1, y1), (x2, y2), color, thickness)

    cv2.imwrite(path, image)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return

    if "stonks" in message.content.lower():
        IMAGE_PATH = "chart_00000.png"
        stock = [0]

        run_test()

        await message.channel.send(
            content="",
            file=discord.File(IMAGE_PATH)
        )


        if os.path.exists(IMAGE_PATH):
            os.remove(IMAGE_PATH)

    await bot.process_commands(message)

bot.run(TOKEN)