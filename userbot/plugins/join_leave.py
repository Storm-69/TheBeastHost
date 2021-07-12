import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import (
    GetAdminedPublicChannelsRequest,
    LeaveChannelRequest,
)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from userbot.utils import admin_cmd, sudo_cmd
# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="pjoin$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="pjoin$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="pjoin$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(ImportChatInviteRequest(bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="join$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="join$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="join$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="join$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="join$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="join$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="join$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="join$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="join$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="join$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="join$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="join$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(functions.channels.JoinChannelRequest(channel=bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="leave$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="leave$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="leave$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="leave$", allow_sudo=True))

async def _(event):
    if event.fwd_from:
        return
    bc = int(event.pattern_match.group(1))
    print(bc)
    event = await edit_or_reply(event, "Trying Leaving...")
    try:
        await event.client(LeaveChannelRequest(bc))
        await event.edit("Succesfully Left")
    except Exception as e:
        await event.edit(str(e))

