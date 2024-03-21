from nextcord.ext import commands 
import colorama
bot = commands.Bot (command_prefix="!")

@bot.command(name= "hi")
async def SendMessage(ctx):
    await ctx.send("Hello World")

@bot.event 
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    print(f"ID : {bot.user.id}")

if __name__ == '__main__':
    bot.run(token)
