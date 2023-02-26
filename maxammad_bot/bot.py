import json
import random
from typing import Union

import discord
from discord import app_commands

from maxammad_bot.resources.replies import responses
from maxammad_bot.create_log import entry

from maxammad_bot.resources.commands import mute
from maxammad_bot.resources.commands import unmute
from maxammad_bot.resources.commands import say


async def send_message(message, user_message, is_private):
    try:
        response: str = responses.handle_response(user_message)
        if is_private is None:
            with open("maxammad_bot/resources/replies/max_quotes.txt", encoding="utf-8") as f:
                response = random.choice(f.read().split("\n"))
        if response is None:
            return
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
    with open("maxammad_bot/tokens.json", encoding="utf-8") as data:
        muh_token = json.load(data)["MAX_TOKEN"]

    intents = discord.Intents.default()
    intents.presences = True
    intents.members = True
    intents.message_content = True

    bot = discord.Client(intents=intents)
    tree = app_commands.CommandTree(bot)

    with open("maxammad_bot/guild_ids.txt", encoding="utf-8") as data:
        guilds = list(map(lambda x: discord.Object(int(x)), data.read().split("\n")))

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running!")

        for guild in guilds:
            await tree.sync(guild=discord.Object(id=guild.id))

        await bot.change_presence(activity=discord.Game(name="with people's feelings."))

        guild_names = list(map(lambda x: x.name, bot.guilds))
        guild_ids = list(map(lambda x: str(x.id), bot.guilds))

        with open("maxammad_bot/guild_ids.json", "w", encoding="utf-8") as file:
            ids = dict(zip(guild_names, guild_ids))
            json.dump(ids, file, indent=2)

        with open("maxammad_bot/guild_ids.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(guild_ids))

        with open("maxammad_bot/guilds_info.txt", "w", encoding="utf-8") as file:
            for guild in bot.guilds:
                file.write(repr(guild) + "\n")

    @tree.command(name="mute", description="ole vait!", guilds=guilds)
    async def mute_command_wrapper(
            interaction: discord.Interaction,
            user: discord.Member,
            seconds: int = 0,
            minutes: int = 0,
            hours: int = 0,
            days: int = 0,
            reason: str = None
    ):
        await mute.mute_command(interaction, user, seconds, minutes, hours, days, reason)

    @tree.command(name="unmute", description="palun privaatsõnume", guilds=guilds)
    async def unmute_wrapper(interaction: discord.Interaction, user: discord.Member, reason: str = None):
        await unmute.unmute(interaction, user, reason)

    @tree.command(name="say", description="Ma rääkida sinu eest.", guilds=guilds)
    async def say_wrapper(interaction: discord.Interaction, message: str, replying_to: str = None):
        await say.say(interaction, message, replying_to)

    @bot.event
    async def on_message(message: discord.Message):

        # await bot.process_commands(message)
        if not message.content:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = message.channel

        server = message.guild.name.replace("/", "-")
        if channel.category:
            category = channel.category.name.replace("/", "-")
        else:
            category = ""
        channel_name = channel.name.replace("/", "-")

        entry(server, category, channel_name,
              f'{username}: "{user_message}"')

        if message.author == bot.user:
            return

        if bot.user.mentioned_in(message):
            await send_message(message, user_message, is_private=None)
        if user_message[0] == "%":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @bot.event
    async def on_reaction_add(reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
        if reaction.emoji.name == "tanel":
            await reaction.message.add_reaction(reaction.emoji)

    bot.run(muh_token)
