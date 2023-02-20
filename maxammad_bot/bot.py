import datetime
import json
import random

from discord.ext import commands
from discord.utils import get
import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response: str = responses.handle_response(user_message)
        if is_private is None:
            with open("max_quotes.txt", encoding="utf-8") as f:
                response = random.choice(f.read().split("\n"))
        if "&ping&" in response:
            response = response.replace("&ping&", message.author.mention)
        if "&name&" in response:
            response = response.replace("&name&", message.author)
        if "&reply&" in response:
            response = response.strip("&reply&")
            await discord.Message.reply(message, response)
            return
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    with open("tokens.json") as f:
        muh_token = json.load(f)["MAX_TOKEN"]
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
        # await client.get_guild(1011692357806198784).get_channel(1011698709215588372).send("Hello, I'm back")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        global channel
        channel = message.channel

        print(f"[{datetime.datetime.now()}] {username} said: '{user_message}' in #{str(channel)}.")

        if client.user.mentioned_in(message):
            await send_message(message, user_message, is_private=None)
        if user_message[0] == "%":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.event
    async def on_disconnect():
        await client.get_guild(1011692357806198784).get_channel(1011698709215588372).send("Good night!")

    client.run(muh_token)
