import discord
from maxammad_bot.create_log import entry


async def say(interaction: discord.Interaction, message: str, replying_to: str):
    server = interaction.guild.name.replace("/", "-")
    if cat := interaction.channel.category:
        category = cat.name.replace("/", "-")
    else:
        category = ""
    channel = interaction.channel.name.replace("/", "-")

    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message(":point_right: :ok_hand:", ephemeral=True)

        entry(server, category, channel,
              f"XXX {interaction.user} tried to say {message} as maxammad23.")
        return

    await interaction.response.send_message("Tehtud", ephemeral=True)

    if replying_to:
        replied_msg: discord.Message = await interaction.channel.fetch_message(int(replying_to))
        await replied_msg.reply(message)
    else:
        await interaction.channel.send(message)

    entry(server, category, channel,
          " " * 22 + f"^^^ This message was ordered by {interaction.user}")
