
from userbot.utils import admin_cmd
from userbot import bot as mafiaopbolte
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import sudo_cmd

# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="gporn$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="gporn$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="gporn$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="gporn$", allow_sudo=True))

async def mafia(fight):
  try:
       await fight.client(ImportChatInviteRequest('Cwcq7jcyTRgyNTA1'))
  except UserAlreadyParticipantError:
        pass
  except:
        await fight.client(ImportChatInviteRequest('Cwcq7jcyTRgyNTA1'))
        return
  async for msg in fight.client.iter_messages(-1001300609856):
   if msg:
    await fight.client.send_message(fight.chat_id, msg)