import time

from userbot import ALIVE_NAME, StartTime, mafiaversion
from mafiabot.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "Mafia User"
MAFIA_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "𝕃𝕖𝕘𝕖𝕟𝕕𝕒𝕣𝕪_𝔸𝔽_𝕄𝕒𝕗𝕚𝕒𝔹𝕠𝕥"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="mafia$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="mafia$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="mafia$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="mafia$", allow_sudo=True))

async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if MAFIA_IMG:
        mafia_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        mafia_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
        mafia_caption += f"__**𝔹𝕆𝕋 𝕊𝕋𝔸𝕋𝕌𝕊**__\n\n"
        mafia_caption += f"**★ 𝕋𝕖𝕝𝕖𝕥𝕙𝕠𝕟 𝕧𝕖𝕣𝕤𝕚𝕠𝕟 :** `1.15.0`\n"
        mafia_caption += f"**★ 𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋 :**`{mafiaversion}`\n"
        mafia_caption += f"**★ 𝕌𝕡𝕥𝕚𝕞𝕖 :** `{uptime}\n`"
        mafia_caption += f"**★ 𝕄𝕒𝕤𝕥𝕖𝕣 :** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, MAFIA_IMG, caption=mafia_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ \n"
            f"__**𝔹𝕆𝕋 𝕊𝕋𝔸𝕋𝕌𝕊**__\n\n"
            f"**★ 𝕋𝕖𝕝𝕖𝕥𝕙𝕠𝕟 𝕧𝕖𝕣𝕤𝕚𝕠𝕟 :** `1.15.0`\n"
            f"**★ 𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋 :** `{mafiaversion}`\n"
            f"**★ 𝕌𝕡𝕥𝕚𝕞𝕖 :** `{uptime}\n`"
            f"**★ 𝕄𝕒𝕤𝕥𝕖𝕣 :** {mention}\n",
        )
