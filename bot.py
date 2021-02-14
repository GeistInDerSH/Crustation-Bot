import discord
from dotenv import load_dotenv
from reaction import Reaction

load_dotenv()

with open('./token.txt', 'r') as fp:
    TOKEN = fp.read(59)

client = discord.Client()

@client.event
async def on_message(message):
    reaction = Reaction(message.author.id, message.content)
    for emoji in reaction.get_reactions():
        await message.add_reaction(emoji)

client.run(TOKEN)
