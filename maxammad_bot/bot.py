import datetime
import json

from discord.ext import commands
from discord.utils import get
import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response: str = responses.handle_response(user_message)
        if "&ping&" in response:
            response = response.replace("&ping&", message.author.mention)
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

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"[{datetime.datetime.now()}] {username} said: '{user_message}' in #{channel}.")

        if user_message[0] == "%":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(muh_token)
