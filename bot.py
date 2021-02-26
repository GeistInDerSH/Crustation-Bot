import discord
from dotenv import load_dotenv
from reaction import Reaction

load_dotenv()

with open('./token.txt', 'r') as fp:
    TOKEN = fp.read(59)

client = discord.Client()

@client.event
async def on_message(message):

    if str(message.author.id) != '759317087192612864':
        reaction = Reaction(message.author.id, message.content)

        if reaction.contains_flags():
            send_message = reaction.get_flag_response()

            if len(send_message) > 0:
                await client.get_channel(message.channel.id).send(send_message)
        else:
            for emoji in reaction.get_reactions():
                await message.add_reaction(emoji)

client.run(TOKEN)
