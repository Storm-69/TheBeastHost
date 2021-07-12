"""Restart or Terminate the bot from any chat
Available Commands:
.restartsys
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import sys
import asyncio
from os import execl
from time import sleep

from mafiabot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import HEROKU_APP, bot

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="restart$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="restart$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="restart$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="restart$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    await event.edit("Restarting **[ ░░░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ █░░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ ██░ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarting **[ ███ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await event.edit("Restarted **[ ✓ ]** ...\nType `.ping` or `.help` to check if I am working 🙂")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="shutdown$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="shutdown$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    await event.edit("**[ ! ]** `Turning off bot now ... Manually turn me on later` ಠ_ಠ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


CmdHelp("power_tools").add_command(
  "restart", None, "Restarts your userbot. Redtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add()
