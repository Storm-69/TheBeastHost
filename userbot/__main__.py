from userbot import sessionone, sessiontwo, sessionthree, sessionfour, sessionfive, sessionsix, sessionseven, sessioneight, sessionnine, sessionten
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, mafiaversion
from pathlib import Path
import asyncio
import telethon.utils


async def add_bot(bot_token):
    await sessionone.start(bot_token)
    sessionone.me = await sessionone.get_me() 
    sessionone.uid = telethon.utils.get_peer_id(sessionone.me)

async def add_bot(bot_token):
    await sessiontwo.start(bot_token)
    sessiontwo.me = await sessiontwo.get_me() 
    sessiontwo.uid = telethon.utils.get_peer_id(sessiontwo.me)

async def add_bot(bot_token):
    await sessionthree.start(bot_token)
    sessionthree.me = await sessionthree.get_me() 
    sessionthree.uid = telethon.utils.get_peer_id(sessionthree.me)

async def add_bot(bot_token):
    await sessionfour.start(bot_token)
    sessionfour.me = await sessionfour.get_me() 
    sessionfour.uid = telethon.utils.get_peer_id(sessionfour.me)

async def add_bot(bot_token):
    await sessionfive.start(bot_token)
    sessionfive.me = await sessionfive.get_me() 
    sessionfive.uid = telethon.utils.get_peer_id(sessionfive.me)

async def add_bot(bot_token):
    await sessionsix.start(bot_token)
    sessionsix.me = await sessionsix.get_me() 
    sessionsix.uid = telethon.utils.get_peer_id(sessionsix.me)

async def add_bot(bot_token):
    await sessionseven.start(bot_token)
    sessionseven.me = await sessionseven.get_me() 
    sessionseven.uid = telethon.utils.get_peer_id(sessionseven.me)

async def add_bot(bot_token):
    await sessioneight.start(bot_token)
    sessioneight.me = await sessioneight.get_me() 
    sessioneight.uid = telethon.utils.get_peer_id(sessioneight.me)

async def add_bot(bot_token):
    await sessionnine.start(bot_token)
    sessionnine.me = await sessionnine.get_me() 
    sessionnine.uid = telethon.utils.get_peer_id(sessionnine.me)

async def add_bot(bot_token):
    await sessionten.start(bot_token)
    sessionten.me = await sessionten.get_me() 
    sessionten.uid = telethon.utils.get_peer_id(sessionten.me)

if len(argv) not in (1, 3, 4):
# ONE
try:
    sessionone.disconnect()
else:
    sessionone.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionone.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionone.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionone.start()
    except Exception as e:
        pass    
        
# TWO        
try:
    sessiontwo.disconnect()
else:
    sessiontwo.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessiontwo.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessiontwo.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessiontwo.start()
    except Exception as e:
        pass    

# THREE
try:
    sessionthree.disconnect()
else:
    sessionthree.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionthree.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionthree.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionthree.start()
    except Exception as e:
        pass    

# FOUR
try:
    sessionfour.disconnect()
else:
    sessionfour.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionfour.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionfour.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionfour.start()
    except Exception as e:
        pass    
 
# FIVE
try:
    sessionfive.disconnect()
else:
    sessionfive.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionfive.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionfive.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionfive.start()
    except Exception as e:
        pass    
        
# SIX
try:
    sessionsix.disconnect()
else:
    sessionsix.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionsix.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionsix.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionsix.start()
    except Exception as e:
        pass    
        
# SEVEN
try:
    sessionseven.disconnect()
else:
    sessionseven.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionseven.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionseven.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionseven.start()
    except Exception as e:
        pass                                           
                 
# EIGHT
try:
    sessioneight.disconnect()
else:
    sessioneight.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessioneight.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessioneight.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessioneight.start()
    except Exception as e:
        pass    
        
# NINE
try:
    sessionnine.disconnect()
else:
    sessionnine.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionnine.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionnine.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionnine.start()
    except Exception as e:
        pass    
 
# TEN
try:
    sessionten.disconnect()
else:
    sessionten.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        sessionten.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        sessionten.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        sessionten.start()
    except Exception as e:
        pass    
        
        
import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


print(f"""YOUR 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 IS READY TO USE! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @MAFIA_USERBOT""")

if len(argv) not in (1, 3, 4):
    try:
        sessionone.disconnect()
    except Exception as e:
        pass
    try:
        sessiontwo.disconnect()
    except Exception as e:
        pass
    try:
        sessionthree.disconnect()
    except Exception as e:
        pass
    try:
        sessionfour.disconnect()
    except Exception as e:
        pass
    try:
        sessionfive.disconnect()
    except Exception as e:
        pass
    try:
        sessionsix.disconnect()
    except Exception as e:
        pass
    try:
        sessionseven.disconnect()
    except Exception as e:
        pass
    try:
        sessioneight.disconnect()
    except Exception as e:
        pass
    try:
        sessionnine.disconnect()
    except Exception as e:
        pass
    try:
        sessionten.disconnect()
    except Exception as e:
        pass
else:
    try:
        sessionone.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessiontwo.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionthree.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionfour.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionfive.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionsix.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionseven.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessioneight.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionnine.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionten.run_until_disconnected()
    except Exception as e:
        pass
