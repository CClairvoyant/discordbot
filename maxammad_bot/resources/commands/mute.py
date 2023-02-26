import random

import discord
from maxammad_bot.create_log import *


async def mute_command(
        interaction: discord.Interaction,
        user: discord.Member,
        seconds: int = 0,
        minutes: int = 0,
        hours: int = 0,
        days: int = 0,
        reason: str = None
):
    server = interaction.guild.name.replace("/", "-")
    if cat := interaction.channel.category:
        category = cat.name.replace("/", "-")
    else:
        category = ""
    channel = interaction.channel.name.replace("/", "-")

    if not interaction.user.guild_permissions.manage_messages:
        await interaction.user.send("No perms idiot")
        await interaction.user.send("https://tenor.com/view/noob-risitas-funny-meme-laughing-gif-18917081")
        await interaction.response.send_message(content=":middle_finger: idi nahui :middle_finger:", ephemeral=True)

        entry(server, category, channel,
              f"XXX {interaction.user} tried to mute {user}"
              + f" for \"{reason}\"" * bool(reason)
              + ".")

        return

    if user.guild_permissions.administrator:
        await interaction.response.send_message(content="Kas sa praegu päriselt proovib admin mute? vabandust palun",
                                                ephemeral=True)

        entry(server, category, channel,
              f"XXX {interaction.user} tried to mute {user} (ADMIN)"
              + f" for \"{reason}\"" * bool(reason)
              + ".")

        return

    if not reason:
        await interaction.response.send_message(random.choice(
            [f"Palun ära tee spammide, ma  olen väsinud küll lugeda kõiki kanalis sellel serveris.{user.mention}",
             f"Tere,{user.mention} mis sul probleem on?Ma saan aidata sulle."]))
    else:
        await interaction.response.send_message(f"tere  miks sa {reason}, {user.mention}? vabandust palun")

    if seconds or minutes or hours or days:
        await user.edit(
            timed_out_until=discord.utils.utcnow() + datetime.timedelta(days=days,
                                                                        hours=hours,
                                                                        minutes=minutes,
                                                                        seconds=seconds))
    else:
        await user.edit(
            timed_out_until=discord.utils.utcnow() + datetime.timedelta(days=28))

    entry(server, category, channel,
          f">>> {interaction.user} muted {user}"
          + f" for \"{reason}\"" * bool(reason)
          + f" for the duration of"
          + f" {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
