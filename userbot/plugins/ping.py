import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from ..cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mafia User"
h1m4n5hu0p = borg.uid

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="hbping$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="hbping$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="hbping$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="hbping$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    animation_interval = 0.2
    animation_ttl = range(0, 26)
    await edit_or_reply(event, "ping....")
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n \n My 🇵 🇮 🇳 🇬  Is : Calculating...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 26])
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await edit_or_reply(event, 
        "‎‎‎‎‎‎‎‎‎⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛⬛📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛📶⬛⬛⬛\n⬛⬛⬛⬛📶⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛📶⬛⬛⬛📶⬛\n⬛⬛📶📶⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶⬛📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n‎‎‎‎‎‎‎‎‎ \n \n My 🇵 🇮 🇳 🇬  Is : {} ms".format(
            ms
        )
    )



# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="ping$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="ping$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="ping$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="ping$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "__**(❛ ᑭσɳց ❜!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**꧁ Pong! ꧂__**\n\n   ⚘ {ms}\n   ⚘ __**My**__ __**Master**__ [{DEFAULTUSER}](tg://user?id={h1m4n5hu0p})"
    )


CmdHelp("ping").add_command(
  "ping", None, "Shows you the ping speed of server"
).add_command(
  "hbping", None, "Shows you the ping speed of server with an animation"
).add()