import discord
import os
import random
import requests
import json
from dotenv import load_dotenv
import datetime
from requests.models import Response


load_dotenv()
client = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')

ppGame = ["Nice try!", "I'm not gonna let you win!", "ARRRRGGGHHHH", "You're weak.", "Level up fool", "You're still a beginner", "PING PING", "PONG PONG", "You think you're slick?",
          "I'm winning", "Fear me!", "Hahahahaha!", "At least your stance looks good. Hmph.", "You are in too deep.", "Brace yourself", "Hmph, I knew you would do that.",
          "I guess this means... I'm the best!", "Whoops! Oh no! Was that too much for you?", "Now that's what I call a critical hit!",
          "This just shows how much better I am than you.", " So predictable.", "I won't let up.", "Feeling lucky?", "Can you keep up?", "Your purpose has ended.", "Looks like you're going to take the L"]

def get_phrasePing():
    num = random.randint(1,100)
    print(num)
    if num%7==0:
        return True
    return False

def get_phrasePong():
    num = random.randint(1,120)
    print(num)
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
        'https://geek-jokes.sameerkumar.website/api?format=json')
    json_data = json.loads(response.text)
    return json_data["joke"]


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
    if message.content.startswith('$hello'):
        await message.channel.send('Goodbye!')
    if message.content.startswith('$ping'):
        phrase = random.choice(ppGame)
        go = get_phrasePing()
        if go:
            await message.channel.send(phrase)
        await message.channel.send('pong!')
    if message.content.startswith('$pong'):
        phrase = random.choice(ppGame)
        go = get_phrasePing()
        if go:
            await message.channel.send(phrase)
        await message.channel.send('ping!')
    if message.content.startswith('$advice'):
        await message.channel.send(get_advice())
    if message.content.startswith('$insult'):
        await message.channel.send(get_insult())
    if message.content.startswith('$joke'):
        await message.channel.send(get_joke())
    if message.content.startswith('$holiday'):
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
    # if "fight" or "attack" or "beat" or "simp" or "pain" or "kick" or "die" in message.content:
    #     await message.channel.send("https://tenor.com/view/fight-couple-kicked-gif-11899011")

# show_holiday()
client.run(TOKEN)
