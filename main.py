import os, ollama, discord
from discord.ext import commands
from discord import Intents
from discord.ui import Button, View

GEMMA_TOKEN = os.environ["MIKAEL_TOKEN"]

intents = Intents.all()
chat_log = []
client = commands.Bot(command_prefix="!", intents=intents, owner_id=1110526906106904626)

@client.event
async def on_ready() -> None:
    try:
        await client.change_presence(
            activity=discord.Streaming(
                name="Ask me anything!", url="https://twitch.tv/gothamchess"
            )
        )
        print(
            f"----- Gemma is Online -----\nServers: {len(client.guilds)}\nMembers: {len(client.users)}"
        )

    except Exception:
        print(Exception)


@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    elif message.content.startswith("!"):
        pass
    
    else:
        if isinstance(message.channel, discord.DMChannel):
            await message.channel.typing()
            num = 1
            while num != 0:
              chat_log.append({"role": "user", "content": message.content})
              chat_call = ollama.chat(model="mistral", messages=chat_log)
              response = chat_call["message"]["content"]
              chat_log.append({"role": "assistant", "content": response})
                    
              await message.channel.send(response)
              num -= 1
            if num == 0:
              break
        else:
            pass
    
    await client.process_commands(message)

client.run(GEMMA_TOKEN)
