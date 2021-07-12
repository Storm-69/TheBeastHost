
import os
import sys
import time
import asyncio
import random
import telethon.utils
from sys import argv
from telethon import TelegramClient, events
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.sessions import StringSession
from userbot.Config import Config
from Config import API_ID, API_HASH, STRING_SESSION, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4 ,STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8 ,STRING_SESSION9, STRING_SESSION10, SUDO_IDS
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, mafiaversion
from pathlib import Path
from var import Var
from userbot.helpers import functions as simpdef


StartTime = time.time()
mafiaversion = "2.0"

os.system("pip install --upgrade pip")

one = STRING_SESSION
two = STRING_SESSION2
three = STRING_SESSION3
four = STRING_SESSION4
five = STRING_SESSION5
six = STRING_SESSION6
seven = STRING_SESSION7
eight = STRING_SESSION8
nine = STRING_SESSION9
ten = STRING_SESSION10


sessionone = ""
sessiontwo = ""
sessionthree = ""
sessionfour = ""
sessionfive = ""
sessionsix = ""
sessionseven = ""
sessioneight = ""
sessionnine = ""
sessionten = ""



que = {}

SUDO_USERS = []
for x in SUDO_IDS:
    SUDO_USERS.append(x)
    
async def start_spam():
    global sessionone
    global sessiontwo
    global sessionthree
    global sessionfour
    global sessionfive
    global sessionsix
    global sessionseven
    global sessioneight
    global sessionten
    global sessionnine
    
    if one:
        session_name = str(one)
        print("String 1 Found")
        sessionone = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 1")
            await sessionone.start()
            botme = await sessionone.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            sessionone = "one"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        sessionone = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionone.start()
        except Exception as e:
            pass
   
    if two:
        session_name = str(two)
        print("String 2 Found")
        sessiontwo = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 2")
            await sessiontwo.start()
            botme = await sessiontwo.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        sessiontwo = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessiontwo.start()
        except Exception as e:
            pass

    if three:
        session_name = str(three)
        print("String 3 Found")
        sessionthree = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 3")
            await  sessionthree.start()
            botme = await sessionthree.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        sessionthree = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionthree.start()
        except Exception as e:
            pass

    if four:
        session_name = str(four)
        print("String 4 Found")
        sessionfour = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 4")
            await sessionfour.start()
            botme = await sessionfour.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        sessionfour = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionfour.start()
        except Exception as e:
            pass

    if five:
        session_name = str(five)
        print("String 5 Found")
        sessionfive = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 5")
            await sessionfive.start()
            botme = await sessionfive.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sessionfive = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionfive.start()
        except Exception as e:
            pass
                  
    if six:
        session_name = str(six)
        print("String 6 Found")
        sessionsix = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 6")
            await sessionsix.start()
            botme = await sessionsix.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        sessionsix = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionsix.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        sessionseven = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 7")
            await sessionseven.start()
            botme = await sessionseven.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        sessionseven = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionseven.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        sessioneight = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 8")
            await sessioneight.start()
            botme = await sessioneight.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        sessioneight = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessioneight.start()
        except Exception as e:
            pass   
        
    if nine:
        session_name = str(nine)
        print("String 9 Found")
        sessionnine = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 9")
            await sessionnine.start()
            botme = await sessionnine.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        sessionnine = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionnine.start()
        except Exception as e:
            pass   
    
  
    if ten:
        session_name = str(ten)
        print("String 10 Found")
        sessionten = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 10")
            await sessionten.start()
            botme = await sessionten.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        sessionten = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionten.start()
        except Exception as e:
            pass 
        
        
loop = asyncio.get_event_loop()
loop.run_until_complete(start_spam())  

     
import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
          

print("""YOUR 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 IS READY TO USE! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @MAFIA_USERBOT""")


CMD_LIST = {}
# for later purposes
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}

# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)

mafia_ID = ["1212368262"]

""" PPE initialization. """

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

import pylast
from pySmartDL import SmartDL
from requests import get
# Bot Logs setup:
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger(__name__)

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except:
    HEROKU_APP = None


    # Check if the config was edited by using the already used variable.
    # Basically, its the 'virginity check' for the config file ;)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

# Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

   
    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    REDIRECTCHANNEL = os.environ.get("REDIRECTCHANNEL", None)

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    
    # Custom Module
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)

    # Upstream Repo
    UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/H1M4N5HU0P/MAFIA-USERBOT.git")

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                      api_secret=LASTFM_SECRET,
                                      username=LASTFM_USERNAME,
                                      password_hash=LASTFM_PASS)
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}


from userbot.helpers import *
from userbot.helpers import functions as mafiadef
from userbot.cmdhelp import CmdHelp

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
