#
# Copyright (C) 2021-2022 by #تعديل وتحديث مطور سورس ايثون
# copyright @EITHON1 @V_V_G

from YukkiMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck, AdminRightsCheckCB

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
STOP_COMMAND_chh = get_command("STOP_COMMAND_chh")


@app.on_message(
    command(STOP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Yukki.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )


@app.on_message(
    command(STOP_COMMAND_chh)
    & filters.channel
    & ~BANNED_USERS
)
@AdminRightsCheckCB
async def stop_music_ch(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Yukki.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    if message.sender_chat:
        mention = f'<a href=tg://user?id={message.chat.id}>{message.chat.title}</a>'
    else:
        mention = message.from_user.mention
    await message.reply_text(
        _["admin_9"].format(mention)
    )
