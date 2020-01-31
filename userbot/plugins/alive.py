"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @FuckingUserbot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`Suru majburi mein kiye the…..Ab maza aa rahe hain (Maa Chod Denge Sbki) ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @venom_vipers\n"
                     "`Bot created by:` [乙Ŧ ツ Venom🕷️🕸️](tg://user?id=1048670849)\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`My Ultra Peru Owner`: {DEFAULTUSER}\n"
                     "[Join Kr Bkl Abhi Tk Nhi Kiya H Toh](https://t.me/hackershubbb)")
