import discord

from maxammad_bot.create_log import entry


async def unmute(interaction: discord.Interaction, user: discord.Member, reason: str = None):
    server = interaction.guild.name.replace("/", "-")
    if cat := interaction.channel.category:
        category = cat.name.replace("/", "-")
    else:
        category = ""
    channel = interaction.channel.name.replace("/", "-")

    if not interaction.user.guild_permissions.manage_messages:
        entry(server, category, channel,
              f"XXX {interaction.user} tried to mute {user}"
              + f" for \"{reason}\"" * bool(reason)
              + ".")
        return

    await interaction.response.send_message(f"{user.mention} kirjutada palun mulle. Ma ootan")
    await interaction.channel.send("kas sa oled praegu siin?")
    await interaction.channel.send("Kas sa oled siin või ei?")
    await interaction.channel.send("Kas sa magab?")

    await user.edit(timed_out_until=None)

    entry(server, category, channel,
          f">>> {interaction.user} unmuted {user}"
          + f" for \"{reason}\"" * bool(reason)
          + ".")
