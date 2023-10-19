import discord
import responses
import racist

DISCORD_TOKEN = "mytoken"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

racistList = []
stream = open("C:/Users/David/Desktop/stuff/PythonVorbereitung/Discord Bot/blacklist.txt")
list = stream.readlines()

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def addRacist(name):
    inList = False

    for i in racistList:
        if i.username == name:
            i.count()
            print("user already in list")
            inList = True
            break

    if inList is False:
        print("user added into list")
        racistList.append(racist.racist(name))

async def checkSentence(input):
    for i in range(len(list)):
        element = list[i].replace("\n", "")
        input = input.upper()
        element = element.upper()
        if element in input:
            l = len(element)
            censored = element[0] + element[1]
            for j in range(2, l):
                censored += '*'
            input = input.replace(element, censored)
            i = 0
            censored = ""
    print(input)
def run_discord_bot():
    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)

        print(f'{username} said: "{user_message}"')

        if user_message[0] == '?':
            user_message = user_message[1:]
            if user_message == "n_score":
                r = responses.get_score(racistList, username)
                await message.author.send(f'{message.author.mention} your score is: {r}')
            elif user_message == "n_top":
                top = responses.get_top(racistList)
                await message.author.send(top)
            else:
                await send_message(message, user_message, is_private = True)
        elif "NIGGA" in user_message.upper() or "NIGGER" in user_message.upper() or "NIGA" in user_message.upper() or "NIGER" in user_message.upper():
            await message.delete()
            await addRacist(username)
        elif user_message == "n_score":
            r = responses.get_score(racistList, username)
            await message.channel.send(f'{message.author.mention} your score is: {r}')
        elif user_message == "n_top":
            if len(racistList) != 0:
                top = responses.get_top(racistList)
                nTop = ""
                z = 1
                for t in top:
                    nTop = nTop + "#" + str(z) + "   " + t.username + " => " + str(t.n_word_counter) + "\n"
                    z += 1
                nTop = "`" + nTop + "`"
                await message.channel.send(nTop)
            else:
                await message.channel.send(f'{message.author.mention} no one said the n-word')
        else:
            await send_message(message, user_message, is_private = False)
        await checkSentence(user_message)
    client.run(DISCORD_TOKEN)
