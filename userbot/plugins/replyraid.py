import asyncio
import random
from userbot.utils import admin_cmd, sudo_cmd
from userbot.helpers import gaali

que = {}

# admin command
@sessionone.on(admin_cmd(incoming=True))
@sessiontwo.on(admin_cmd(incoming=True))
@sessionthree.on(admin_cmd(incoming=True))
@sessionfour.on(admin_cmd(incoming=True))
@sessionfive.on(admin_cmd(incoming=True))
@sessionsix.on(admin_cmd(incoming=True))
@sessionseven.on(admin_cmd(incoming=True))
@sessioneight.on(admin_cmd(incoming=True))
@sessionnine.on(admin_cmd(incoming=True))
@sessionten.on(admin_cmd(incoming=True))
# sudo command
@sessionone.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessiontwo.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessionthree.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessionfour.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessionfive.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessionsix.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessionseven.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessioneight.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessionnine.on(sudo_cmd(incoming=True, allow_sudo=True))
@sessionten.on(sudo_cmd(incoming=True, allow_sudo=True))

async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(gaali.RRAID)),
            reply_to=event.message.id,
        )
# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="replyraid$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="replyraid$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="replyraid$", allow_sudo=True))

async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")


# admin command
@sessionone.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessiontwo.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessionthree.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessionfour.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessionfive.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessionsix.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessionseven.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessioneight.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessionnine.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
@sessionten.on(admin_cmd(outgoing=True, pattern="dreplyraid$"))
# sudo command
@sessionone.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessiontwo.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessionthree.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessionfour.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessionfive.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessionsix.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessionseven.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessioneight.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessionnine.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))
@sessionten.on(sudo_cmd(pattern="dreplyraid$", allow_sudo=True))

async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
