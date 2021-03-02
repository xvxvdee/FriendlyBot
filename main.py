import discord
from discord import channel
from discord.enums import Status
from discord.ext import commands
import os
import random
import requests
import json
from dotenv import load_dotenv
import datetime
from requests.models import Response
from joke.jokes import *

load_dotenv()
client = commands.Bot(command_prefix='&')
TOKEN = os.getenv('DISCORD_TOKEN')

ppGame = ["Nice try!", "I'm not gonna let you win!", "ARRRRGGGHHHH", "You're weak.", "Level up fool", "You're still a beginner", "PING PING", "PONG PONG", "You think you're slick?",
          "I'm winning", "Fear me!", "Hahahahaha!", "At least your stance looks good. Hmph.", "You are in too deep.", "Brace yourself", "Hmph, I knew you would do that.",
          "I guess this means... I'm the best!", "Whoops! Oh no! Was that too much for you?", "Now that's what I call a critical hit!",
          "This just shows how much better I am than you.", " So predictable.", "I won't let up.", "Feeling lucky?", "Can you keep up?", "Your purpose has ended.", "Looks like you're going to take the L"]

toxic = ["Don't be fat.", "I think being less fat might help.", "You're jobless and want advice lol.","You may simp for that woman's gorilla grip.", "Finish your work stupid bitch.", "You're a compsci major, whiteboard your life problems", "3 x 23", "You skipped 5 lectures and have 2 pending assignments... I rest my case.", "Get your g2 license.", "Worst case Ontario, you miss a 406 midterm.", "Being fat is temporary, therefore I temporarily hate you.", "Imagine paying $600 for no coop placement.", "You're a low level programmer.", "I hope you're doing well and finish all your exams.", "Rosemary.", "Shut up you literally have a girlfriend.", "Shut up you literally have a job.", "I HATE IT HERE TOO. DONT ASK ME FOR ADVICE.","BEEP BOOP, fat humanoid detected!", "Imagine being a front end developer.", "4.00+ gpa and for what? No coop placement.", "Checkmate Liberal", "Indian guys are dming Kami, you cant be that down bad.", "You're probably an international student... Sorry.", "You have a smaller pp than Igor", "No way man.. NO WAY NO WAY.", "Jon.. help me with my school work", "I LOVE KYLE CHOO MANG.", "My little pogchamp, everything is okay.", "You're my little choo mang.", "You're sus", "Trust me im a computer science major, taking the earths radius and multiplying by the solar mass of Messier 61 we can achieve our horizontal displacement value. This allows us to derive the integral interpolation towards the linear space of a 9D vector in the conscience space. This vector separation allows the atomic sub division to then activate what we call as sleep homogeneous distribution. This state allows a person to maintain their last conscience thought told in a social setting. So therefore you're wrong", "I've been single for 5 years. You don't know the struggle.", "STUPIDITY DETECTED", "Professor Edey is available for appointments.", "Ethan, I thought of adding a fat joke, but I take it back.", "IGOR YOU'RE LITERALLY SO CUTE AND HANDSOME", "At least you're not washed up immortal who lost their smurf to a hacker", "Sharif is fat", "Kami a gold digger", "Dylan uses Jon for work.. But you didn't hear that from me."]
botStatusOn = True
samId= "186269007676964864"
deeId ="601912927959777300"
todo = {}
def add_item_existingKey(key,ele):
    response=""
    if key in todo:
        if len(todo.get(key))==0:
            todo[key]=[ele]
        else:
            todo[key].append(ele)
        response="Todo list for this week has been successfully updated."
    else:
        response="Class is not in Todo list. Update failed."
    return response

def remove_item_existingKey(key,ele):
    response=""
    if key in todo:
        if len(todo.get(key))==0:
            response="There is nothing to remove."
        else:
            todo[key].remove(ele)
        response="Todo list for this week has been successfully updated."
    else:
        response="Class is not in Todo list. Update failed."
    return response

def clear_todo():
    todo.clear()
    return "Todo list for the week has been cleared successfully."

def delete_key(key):
    if key in todo:
        todo.pop(key)
        return "Todo list for the week has been updated successfully."
    else:
        return "Class is not in Todo list. Update failed."

def add_newKey(key,ele):
    if key in todo:
        return "This class is already on the todo list. Please update list"
    else:
        todo[key]=ele
        return "Todo list for the week has been updated successfully."

def show_todo():
    msg="TODO THIS WEEK\n\n"
    if len(todo)==0:
        return "Empty.."
    for i in todo.keys():
        msg+= str(i.upper())+":\n"
        for j in todo.get(i):
            msg+="-->"+str(j)+"\n"
        msg+="\n\n"
    return msg

def get_phrasePing():
    num = random.randint(1,100)
    if num%7==0:
        return True
    return False

def get_phrasePong():
    num = random.randint(1,120)
    if num%8==0:
        return True
    return False
   
def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    json_data = json.loads(response.text)
    return json_data['slip']['advice']

def get_insult():
    response = requests.get(
        "https://evilinsult.com/generate_insult.php?lang=en&type=json")
    json_data = json.loads(response.text)
    return json_data['insult']

def get_joke():
    response = requests.get(
      'https://official-joke-api.appspot.com/jokes/random')
    json_data = json.loads(response.text)
    joke = json_data['setup'] +"\n"+json_data['punchline']
    return joke

def get_joke2():
    response = requests.get("https://v2.jokeapi.dev/joke/Programming,Dark,Pun")
    json_data = json.loads(response.text)
    type = json_data['type']
    joke = ""
    if type == "twopart":
        joke = json_data['setup'] +"\n"+json_data['delivery']
    else:
        joke=  json_data['joke']
    return joke

def show_holiday():
    dt = []
    d = datetime.datetime.now()
    date = str(d.year)+"-"+str(d.month)+"-"+str(d.strftime("%d"))
    response = requests.get(
        "https://date.nager.at/api/v2/PublicHolidays/2021/CA")
    data = json.loads(response.text)
    for i in data:
        if i['date'] == date:
            dt.append(i['name'])
    return dt

def checkBotStatus():
    return botStatusOn

def updateStatus(num):
    global botStatusOn
    if num==1:
        botStatusOn=StatusOn()
    if num==0:
        botStatusOn=StatusOff()
    return botStatusOn

def StatusOff():
    print("OFF")
    return False
def StatusOn():
    print("ON")
    return True


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases=['startup'])
async def _startup(ctx):
    print("Start up",checkBotStatus())
    if not checkBotStatus():    
        updateStatus(1)
        await ctx.channel.send("If I back it up, is it fat enough? I know you missed me")
    return

@client.command(aliases=['shutdown'])
async def _shutdown(ctx):
    print("Shut down",checkBotStatus())
    if checkBotStatus():
        updateStatus(0)
        await ctx.channel.send("Corvette, corvette. Hopped out the mf server like jet.")
    return  

@client.command(aliases=['lc'])
async def _lc(ctx):
    embed=discord.Embed(title="Commands for Friendly Bot", color=0x67ec65)
    embed.add_field(name="&startup", value="Startup the bot", inline=False)
    embed.add_field(name="&shutdown", value="Shut the bot down for a bit", inline=False)
    embed.add_field(name="&lc", value="List commands", inline=False)
    embed.add_field(name="&addSam", value="(Only for sam) Add to his list of toxic sayings.", inline=False)
    embed.add_field(name="&pong", value="ping", inline=False)
    embed.add_field(name="&ping", value="pong", inline=False)
    embed.add_field(name="&samSays", value="Get some wisdom from Sam", inline=False)
    embed.add_field(name="&insult", value="Get insulted", inline=False)
    embed.add_field(name="&holidays", value="Check if there are any holidays today.", inline=False)
    embed.add_field(name="&advice", value="Get some advice", inline=False)
    embed.add_field(name="&joke", value="Ahaha hah.", inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['addSam'])
async def _addSam(ctx,*,lstElement):
    global toxic
    if checkBotStatus():
        id = ctx.author.id
        if str(id) == samId:
            toxic.append(lstElement)
            await ctx.send("The command &samSays has been updated.")
            print(toxic)
        elif  str(id) != samId:
            await ctx.send("The update has failed.")
            print(id)

@client.command(aliases=['pong'])
async def _pong(ctx):
    print("check",checkBotStatus())
    if checkBotStatus():
        phrase = random.choice(ppGame)
        go = get_phrasePing()
        await ctx.channel.send('ping!')
        if go:
            await ctx.channel.send(phrase)
  
@client.command(aliases=['ping'])
async def _ping(ctx):
    if checkBotStatus():
        phrase = random.choice(ppGame)
        go = get_phrasePing()
        await ctx.channel.send('pong!')
        if go:
            await ctx.channel.send(phrase)

@client.command(aliases=['samSays'])
async def _samBeingToxic(ctx):
    if checkBotStatus():
        phrase = random.choice(toxic)
        await ctx.channel.send(phrase)

@client.command(aliases=['insult'])
async def _insult(ctx):
    if checkBotStatus():
        await ctx.channel.send(get_insult())

@client.command(aliases=['joke'])
async def _joke(ctx):
    if checkBotStatus():
        lst_joke = [get_joke(),get_joke2()]
        await ctx.channel.send(random.choice(lst_joke))

@client.command(aliases=['holidays'])
async def _holidays(ctx):
    if checkBotStatus():
        lst = show_holiday()
        if len(lst) == 0:
            await ctx.channel.send("No holidays today.")
        else:
            holidays = (", ").join(lst)
            await ctx.channel.send("Today we celebrate: " + holidays)

@client.command(aliases=['advice'])
async def _advice(ctx):
    if checkBotStatus():
        await ctx.channel.send(get_advice())


client.run(TOKEN)
