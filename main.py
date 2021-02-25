import discord
import os
import random
import requests
import json
from dotenv import load_dotenv
import datetime
from requests.models import Response
from joke.jokes import *



load_dotenv()
client = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')

ppGame = ["Nice try!", "I'm not gonna let you win!", "ARRRRGGGHHHH", "You're weak.", "Level up fool", "You're still a beginner", "PING PING", "PONG PONG", "You think you're slick?",
          "I'm winning", "Fear me!", "Hahahahaha!", "At least your stance looks good. Hmph.", "You are in too deep.", "Brace yourself", "Hmph, I knew you would do that.",
          "I guess this means... I'm the best!", "Whoops! Oh no! Was that too much for you?", "Now that's what I call a critical hit!",
          "This just shows how much better I am than you.", " So predictable.", "I won't let up.", "Feeling lucky?", "Can you keep up?", "Your purpose has ended.", "Looks like you're going to take the L"]

toxic =adviceList = ["Don't be fat.", "I think being less fat might help.", "You're jobless and want advice lol.","You may simp for that woman's gorilla grip.", "Finish your work stupid bitch.", "You're a compsci major, whiteboard your life problems", "3 x 23", "You skipped 5 lectures and have 2 pending assignments... I rest my case.", "Get your g2 license.", "Worst case Ontario, you miss a 406 midterm.", "Being fat is temporary, therefore I temporarily hate you.", "Imagine paying $600 for no coop placement.", "You're a low level programmer.", "I hope you're doing well and finish all your exams.", "Rosemary.", "Shut up you literally have a girlfriend.", "Shut up you literally have a job.", "I HATE IT HERE TOO. DONT ASK ME FOR ADVICE.","BEEP BOOP, fat humanoid detected!", "Imagine being a front end developer.", "4.00+ gpa and for what? No coop placement.", "Checkmate Liberal", "Indian guys are dming Kami, you cant be that down bad.", "You're probably an international student... Sorry.", "You have a smaller pp than Igor", "No way man.. NO WAY NO WAY.", "Jon.. help me with my school work", "I LOVE KYLE CHOO MANG.", "My little pogchamp, everything is okay.", "You're my little choo mang.", "You're sus", "Trust me im a computer science major, taking the earths radius and multiplying by the solar mass of Messier 61 we can achieve our horizontal displacement value. This allows us to derive the integral interpolation towards the linear space of a 9D vector in the conscience space. This vector separation allows the atomic sub division to then activate what we call as sleep homogeneous distribution. This state allows a person to maintain their last conscience thought told in a social setting. So therefore you're wrong", "I've been single for 5 years. You don't know the struggle.", "STUPIDITY DETECTED", "Professor Edey is available for appointments.", "Ethan, I thought of adding a fat joke, but I take it back.", "IGOR YOU'RE LITERALLY SO CUTE AND HANDSOME", "At least you're not washed up immortal who lost their smurf to a hacker", "Sharif is fat", "Kami a gold digger", "Dylan uses Jon for work.. But you didn't hear that from me."]

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


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('&ping'):
        phrase = random.choice(ppGame)
        go = get_phrasePing()
        if go:
            await message.channel.send(phrase)
        await message.channel.send('pong!')
    if message.content.startswith('&pong'):
        phrase = random.choice(ppGame)
        go = get_phrasePing()
        if go:
            await message.channel.send(phrase)
        await message.channel.send('ping!')
    if message.content.startswith('&samSays'):
        phrase = random.choice(toxic)
        await message.channel.send(phrase)
    
    if message.content.startswith('&advice'):
        await message.channel.send(get_advice())
    if message.content.startswith('&insult'):
        await message.channel.send(get_insult())
    if message.content.startswith('&joke'):
        lst_joke = [get_joke(),get_joke2()]
        await message.channel.send(random.choice(lst_joke))
    if message.content.startswith('&holiday'):
        lst = show_holiday()
        if len(lst) == 0:
            await message.channel.send("No holidays today.")
        else:
            holidays = (", ").join(lst)
            await message.channel.send("Today we celebrate: " + holidays)
    if "birth" in message.content:
        await message.channel.send("Who's the father?")
    if "love" in message.content:
        await message.channel.send("Someone is being a simp...")
    if "meow" in message.content:
        await message.channel.send("You must be in the wrong channel.")
    if message.content.startswith('cat'):
        await message.channel.send("Get that garbage out of here!")
    if "val" or "valorant" in message.content:
        await message.channel.send("Shouldn't you be grinding? It's midterm season. Are you even plat? That's what I thought buddy!")
    if message.content.startswith("&testing"):
        await message.channel.send(message)

# show_holiday()
client.run(TOKEN)
