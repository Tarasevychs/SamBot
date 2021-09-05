import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def what(ctx):
    emb = discord.Embed(title=str('L-help'), color=0xe5e500, )
    emb.add_field(name="commands", value="``>what`` - this message\n"
                                         "``>news``- news from hackernews\n"
                                         "``>github``- github repository",
                  inline=False)
    await ctx.send(embed=emb)


@bot.event
async def on_member_join(member, ):
    channel = bot.get_channel(878252882384785450)
    role = discord.utils.get(member.guild.roles, id=878265807535214592)

    await member.add_roles(role)
    await channel.send(embed=discord.Embed(description=f'hello ``{member.name}``!', color=0xe5e500))

@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/Tarasevychs/LDiscordBot")

@bot.command()
async def news(ctx):
    count = 1
    url = "https://news.ycombinator.com/news?p=1"
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    teme = soup.find_all("td", class_="title")
    for temes in teme:
        temes = temes.find("a", {'class': 'storylink'})
        if temes is not None and not 'github.com' in str(temes.text) and count < 6:
            sublink = temes.get('href')
            emb = discord.Embed(title=str(temes.text), url=str(sublink), description=f'#{count} in hackernews',
                                color=0xe5e500)
            await ctx.send(embed=emb)
            count += 1


bot.run('token')
