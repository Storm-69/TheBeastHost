# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio
import base64
import os

from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from mafiabot.Config import Config

LOGGER = Config.PLUGIN_CHANNEL
SUDO_WALA = Config.SUDO_USERS

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="spam$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="spam$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="spam$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="spam$", allow_sudo=True))

async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="bigspam$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="bigspam$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="bigspam$", allow_sudo=True))

async def bigspam(mafia):
    if not mafia.text[0].isalpha() and mafia.text[0] not in ("/", "#", "@", "!"):
        mafia_msg = mafia.text
        mafiabot_count = int(mafia_msg[9:13])
        mafia_spam = str(mafia.text[13:])
        for i in range(1, mafiabot_count):
            await mafia.respond(mafia_spam)
        await mafia.delete()
        if LOGGER:
            await mafia.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="dspam$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="dspam$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="dspam$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="dspam$", allow_sudo=True))

async def spammer(e):
    if e.fwd_from:
        return
    input_str = "".join(e.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    spam_message = str(input_str.split(" ", 2)[2])
    await e.delete()
    for _ in range(counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)


#@register(outgoing=True, pattern="^.mspam (.*)")

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="mspam$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="mspam$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="mspam$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="mspam$", allow_sudo=True))

async def tiny_pic_spam(e):
    sender = await e.get_sender()
    me = await e.client.get_me()
    if not sender.id == me.id and not SUDO_WALA:
        return await e.reply("`Sorry sudo users cant access this command..`")
    try:
        await e.delete()
    except:
        pass
    try:
        counter = int(e.pattern_match.group(1).split(" ", 1)[0])
        reply_message = await e.get_reply_message()
        if (
            not reply_message
            or not e.reply_to_msg_id
            or not reply_message.media
            or not reply_message.media
        ):
            return await e.edit("```Reply to a pic/sticker/gif/video message```")
        message = reply_message.media
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, message)
    except:
        return await e.reply(
            f"**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`"
        )


CmdHelp("spam").add_command(
  "spam", "<number> <text>", "Sends the text 'X' number of times.", ".spam 99 Hello"
).add_command(
  "mspam", "<reply to media> <number>", "Sends the replied media (gif/ video/ sticker/ pic) 'X' number of times", ".mspam 100 <reply to media>"
).add_command(
  "dspam", "<delay> <spam count> <text>", "Sends the text 'X' number of times in 'Y' seconds of delay", ".dspam 5 100 Hello"
).add_command(
  "bigspam", "<count> <text>", "Sends the text 'X' number of times. This what mafiabot iz known for. The Best BigSpam Ever", ".bigspam 5000 Hello"
).add()