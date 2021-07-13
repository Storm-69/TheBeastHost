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
 
# FIVE
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
        
# SIX
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
        
# SEVEN
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
                 
# EIGHT
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
        
# NINE
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
 
# TEN
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
