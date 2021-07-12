from userbot.utils import admin_cmd 
from userbot import bot as mafiaopbolte
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import sudo_cmd

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="gspam$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="gspam$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="gspam$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="gspam$", allow_sudo=True))

async def mafia(fight):
  try:
       await fight.client(ImportChatInviteRequest('hE8sJZOZ-L9mODA1'))
  except UserAlreadyParticipantError:
        pass
  except:
        await fight.client(ImportChatInviteRequest('hE8sJZOZ-L9mODA1'))
        return
  async for msg in fight.client.iter_messages(-1001475750241):
   if msg:
    await fight.client.send_message(fight.chat_id, msg)