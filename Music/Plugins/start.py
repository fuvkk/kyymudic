import asyncio
import yt_dlp
import psutil

from Music.config import GROUP, CHANNEL
from Music import (
    ASSID,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    OWNER,
    SUDOERS,
    app,
)
from Music.MusicUtilities.database.chats import is_served_chat
from Music.MusicUtilities.database.queue import remove_active_chat
from Music.MusicUtilities.database.sudo import get_sudoers
from Music.MusicUtilities.database.assistant import (_get_assistant, get_as_names, get_assistant,
                        save_assistant)
from Music.MusicUtilities.database.auth import (_get_authusers, add_nonadmin_chat, delete_authuser,
                   get_authuser, get_authuser_count, get_authuser_names,
                   is_nonadmin_chat, remove_nonadmin_chat, save_authuser)
from Music.MusicUtilities.database.blacklistchat import blacklist_chat, blacklisted_chats, whitelist_chat
from Music.MusicUtilities.helpers.admins import ActualAdminCB
from Music.MusicUtilities.helpers.inline import personal_markup, setting_markup
from Music.MusicUtilities.helpers.inline import (custommarkup, dashmarkup, setting_markup,
                          start_pannel, usermarkup, volmarkup)
from Music.MusicUtilities.helpers.thumbnails import down_thumb
from Music.MusicUtilities.helpers.ytdl import ytdl_opts
from Music.MusicUtilities.tgcallsrun.music import pytgcalls
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


def start_pannel():
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ​", url=f"https://t.me/{GROUP}"),
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{CHANNEL}"),
        ],
        [
            InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅ​ 📚", url="https://telegra.ph/ҡʏʏ-ᴇx-12-15"),
        ],
        [
            InlineKeyboardButton("🌐 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🌐", url="https://github.com/muhammadrizky16/KyyMusic"),
        ],
    ]
    return (
        "🎛 **{BOT_NAME} Merupakan salah satu dari bot telegram yang bisa memutar musik di grup**",
        buttons,
    )


pstart_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ᴛᴏ ɢʀᴏᴜᴘ​ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(text="✨ sᴜᴘᴘᴏʀᴛ​", url=f"https://t.me/{GROUP}"),
            InlineKeyboardButton("✨ ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{CHANNEL}"),
        ],
        [
            InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅ ​📚", url="https://telegra.ph/ҡʏʏ-ᴇx-12-15"),
        ],
        [
            InlineKeyboardButton("🌐 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🌐", url="https://github.com/muhammadrizky16/KyyMusic"),
        ],
    ]
)
welcome_captcha_group = 2


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**[ᴘᴀᴠᴀɴ ᴛᴜɴᴇꜱ](https://t.me/Creator_Pavan) ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴏɴ ᴜʀ ɢʀᴏᴜᴘꜱ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ɴᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ'ꜱ ᴠɪᴅᴇᴏ ᴄʜᴀᴛꜱ ꜰᴇᴀᴛᴜʀᴇ..!

💁🏻‍♂️ ᴜꜱᴇ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴘᴀᴠᴀɴ ᴛᴜɴᴇꜱ ᴏᴘ ᴍᴜꜱɪᴄ ʙᴏᴛ ꜱʏꜱᴛᴇᴍ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                
                
                [InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ", callback_data="cbcmds"),
                    InlineKeyboardButton("ᴄʀᴇᴅɪᴛ", callback_data="cbcredit"),
                ], 
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴘᴀᴠᴀɴ ᴛᴜɴᴇꜱ :**

» ꜰɪʀꜱᴛ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ. 

» ᴛʜᴇɴ, ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴏʀ ᴀɴᴅ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.

» ᴀꜰᴛᴇʀ ᴘʀᴏᴍᴏᴛɪɴɢ ᴍᴇ, ᴛʏᴘᴇ /reload ɪɴ ɢʀᴏᴜᴘ ᴛᴏ ʀᴇꜰʀᴇꜱʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ.

» ᴀᴅᴅ @PavanTunesAssistant ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ʜᴇʀ.

» ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ꜰɪʀꜱᴛ ʙᴇꜰᴏʀᴇ ꜱᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.

» ɪꜰ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ, ᴍᴀᴋᴇ ꜱᴜʀᴇ ɪꜰ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ, ᴏʀ ᴛʏᴘᴇ /userbotleave ᴛʜᴇɴ ᴛʏᴘᴇ /userbotjoin ᴀɢᴀɪɴ.

**ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ꜰᴏʟʟᴏᴡ-ᴜᴘ Qᴜᴇꜱᴛɪᴏɴꜱ ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ ᴏʀ ᴀ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴇʟʟ ɪᴛ ᴏɴ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ʜᴇʀᴇ: @CreatorPavanSupport**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbcredit"))
async def cbcredit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴀʙᴏᴜᴛ ᴄʀᴇᴅɪᴛ :**

» ᴘᴀᴠᴀɴ ᴛᴜɴᴇꜱ ɪꜱ ᴛʜᴇ ʀᴇᴅᴇꜱɪɢɴᴇᴅ ᴠᴇʀꜱɪᴏɴ ᴏꜰ **ᴠᴇᴇᴢ**. 

» ꜰʀᴏᴍ ᴏᴜʀ ᴀʙɪʟɪᴛʏ ᴡᴇ ᴛʀʏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴇᴀꜱɪᴇʀ ᴀɴᴅ ᴛʀʏ ᴛᴏ ɢɪᴠᴇ ᴀ ʙᴇꜱᴛ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ.

» ᴛʜᴇ ᴄʀᴇᴅɪᴛ ᴏꜰ ᴍᴀɪɴ ꜱᴏᴜʀᴄᴇ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɢᴏɪɴɢ ᴛᴏ **ʟᴇᴠɪɴᴀ-x**.

» ᴛʜᴇ ᴡʜᴏʟᴇ ᴄʀᴇᴅɪᴛ ᴏꜰ ʀᴇᴅᴇꜱɪɢɴɪɴɢ ᴀɴᴅ ɢɪᴠɪɴɢ ᴀ ɴɪᴄᴇ ʟᴏᴏᴋ ɪꜱ ɢᴏɪɴɢ ᴛᴏ **ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ**.

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""💞 **ʜᴇʟʟᴏᴡ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» ꜰᴏʀ ᴋɴᴏᴡɪɴɢ ᴀ ᴄᴏᴍᴍᴀɴᴅ ʟɪꜱᴛ ᴏꜰ ʙʀᴏᴋᴇɴ ᴊᴜꜱᴛ ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴘʟᴀʏ", callback_data="cbplay"), 
                    InlineKeyboardButton("ꜱᴜᴅᴏ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("ᴀᴅᴍɪɴ", callback_data="cbadmin"), 
                    InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data="cbvideo"),
                ],[
                    InlineKeyboardButton("ᴘᴀᴠᴀɴ", callback_data="cbpavan"), 
                    InlineKeyboardButton("ᴏᴡɴᴇʀ", callback_data="cbowner"),
                ],[
                    InlineKeyboardButton("ꜱᴛʀᴇᴀᴍ", callback_data="cbstream"), 
                    InlineKeyboardButton("ꜱᴛᴀᴛᴜꜱ", callback_data="cbstatus"),
                ],[
                    InlineKeyboardButton("ᴀʟɪᴠᴇ", callback_data="cbalive"), 
                    InlineKeyboardButton("ᴀꜱꜱɪꜱᴛᴀɴᴛ", callback_data="cbass"),
                ],[
                    InlineKeyboardButton("ʙᴀꜱɪᴄ", callback_data="cbbasic"),
                    InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ", callback_data="cbdownload"),
                ],[
                    InlineKeyboardButton("ᴍᴇɴᴜ ꜱᴇᴛᴛɪɴɢꜱ", callback_data="cbsetting"),
                ],[
                    InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbstart")
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴘᴀᴠᴀɴ ʙᴀꜱɪᴄ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /play [ꜱᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ] - ᴘʟᴀʏ ᴍᴜꜱɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ 
» /stream [Qᴜᴇʀʏ/ʟɪɴᴋ] - ꜱᴛʀᴇᴀᴍ ᴛʜᴇ ʏᴛ ʟɪᴠᴇ/ʀᴀᴅɪᴏ ʟɪᴠᴇ ᴍᴜꜱɪᴄ 
» /vplay [ᴠɪᴅᴇᴏ ɴᴀᴍᴇ/ʟɪɴᴋ] - ᴘʟᴀʏ ᴠɪᴅᴇᴏ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ 
» /vstream - ᴘʟᴀʏ ʟɪᴠᴇ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴛ ʟɪᴠᴇ/ᴍ3ᴜ8 
» /playlist - ꜱʜᴏᴡ ʏᴏᴜ ᴛʜᴇ ᴘʟᴀʏʟɪꜱᴛ 
» /video [Qᴜᴇʀʏ] - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ 
» /song [Qᴜᴇʀʏ] - ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ 
» /lyrics [Qᴜᴇʀʏ] - ꜱᴄʀᴀᴘ ᴛʜᴇ ꜱᴏɴɢ ʟʏʀɪᴄ 
» /search [Qᴜᴇʀʏ] - ꜱᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ  
» /ping - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ ꜱᴛᴀᴛᴜꜱ 
» /uptime - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ ꜱᴛᴀᴛᴜꜱ 
» /alive - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴꜰᴏ [ɪɴ ɢʀᴏᴜᴘ]

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴘᴀᴠᴀɴ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /pause - ᴘᴀᴜꜱᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 
» /resume - ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 
» /skip - ꜱᴡɪᴛᴄʜ ᴛᴏ ɴᴇxᴛ ꜱᴛʀᴇᴀᴍ 
» /stop - ꜱᴛᴏᴘ ᴛʜᴇ ꜱᴛʀᴇᴀᴍɪɴɢ 
» /vmute - ᴍᴜᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 
» /vunmute - ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 
» /volume 1-200 - ᴀᴅᴊᴜꜱᴛ ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ᴏꜰ ᴍᴜꜱɪᴄ (ᴜꜱᴇʀʙᴏᴛ ᴍᴜꜱᴛ ʙᴇ ᴀᴅᴍɪɴ) 
» /reload - ʀᴇʟᴏᴀᴅ ʙᴏᴛ ᴀɴᴅ ʀᴇꜰʀᴇꜱʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ 
» /userbotjoin - ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ 
» /userbotleave - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴘᴀᴠᴀɴ ꜱᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /rmw - ᴄʟᴇᴀɴ ᴀʟʟ ʀᴀᴡ ꜰɪʟᴇꜱ 
» /rmd - ᴄʟᴇᴀɴ ᴀʟʟ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜰɪʟᴇꜱ 
» /sysinfo - ꜱʜᴏᴡ ᴛʜᴇ ꜱʏꜱᴛᴇᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 
» /update - ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ 
» /restart - ʀᴇꜱᴛᴀʀᴛ ʏᴏᴜʀ ʙᴏᴛ 
» /leaveall - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀʟʟ ɢʀᴏᴜᴘ

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbplay"))
async def cbplay(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ᴘʟᴀʏ ᴄᴏᴍᴍᴀɴᴅ :**

» /play - ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀ ᴘʟᴀʏɪɴɢ ᴜʀ ꜱᴏɴɢ. ᴊᴜꜱᴛ ᴛʏᴘᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ɪɴ ꜰʀᴏɴᴛ ᴏꜰ ᴛʜɪꜱ ᴛʏᴘᴇ ᴜʀ ꜱᴏɴɢ ɴᴀᴍᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ.   

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbvideo"))
async def cbvideo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ᴠɪᴅᴇᴏ ᴄᴏᴍᴍᴀɴᴅ :**

» /vplay - ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ꜰᴏʀ ᴘʟᴀʏɪɴɢ ᴀ ᴠɪᴅᴇᴏ ɪɴ ᴜʀ ɢʀᴏᴜᴘꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. ᴜꜱᴇ ɪᴛ ʟɪᴋᴇ ᴀ ᴘʟᴀʏ ᴄᴏᴍᴍᴀɴᴅ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbpavan"))
async def cbpavan(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ꜱᴘᴇᴄɪᴀʟ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /pavan - ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ꜰᴏʀ ᴀ ᴄʜᴇᴄᴋɪɴɢ ɪꜱ ʙᴏᴛ ɪꜱ ᴡᴏʀᴋɪɴɢ ᴏʀ ɴᴏᴛ ? 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbass"))
async def cbass(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /userbotjoin - ꜰᴏʀ ᴊᴏɪɴɪɴɢ ᴀꜱꜱɪꜱᴛᴀɴᴛ. 
» /userbotleave - ꜰᴏʀ ʀᴇᴍᴏᴠᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛ. 
» @PavanTunesAssistant - ᴀᴅᴅ ᴛʜɪꜱ ᴀꜱꜱɪꜱᴛᴀɴᴛ ꜰᴏʀ ᴘʟᴀʏɪɴɢ ᴀ ꜱᴏɴɢꜱ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbstream"))
async def cbstream(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ꜱᴛʀᴇᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /stream - ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ꜰᴏʀ ᴘʟᴀʏɪɴɢ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ꜱᴇʀᴠᴇʀ. 
» /vplay - ᴛʏᴘᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ɢɪᴠᴇ ʟɪᴠᴇ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ ꜰᴏʀ ꜱᴛʀᴇᴀᴍɪɴɢ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbstatus"))
async def cbstatus(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ꜱᴛᴀᴛᴜꜱ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /uptime - ꜰᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ. 
» /alive - ꜰᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ. 
» /ping - ꜰᴏʀ ᴘɪɴɢ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbalive"))
async def cbalive(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ʟɪᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /alive - ꜰᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴀʟʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ʙᴏᴛ ꜱʏꜱᴛᴇᴍ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /sysinfo - ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴏɴʟʏ ꜰᴏʀ ᴏᴡɴᴇʀ ᴍᴀꜱᴛᴇʀ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ꜰᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ ᴘʀᴏᴄᴇꜱꜱᴏʀ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbdownload"))
async def cbdownload(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /song - ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜꜱɪᴄ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ꜱᴇʀᴠᴇʀ ɪɴ ᴍᴘ3 ꜰᴏʀᴍᴀᴛ. 
» /video - ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜꜱɪᴄ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ꜱᴇʀᴠᴇʀ ɪɴ ᴠɪᴅᴇᴏ ꜰᴏʀᴍᴀᴛ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )
@Client.on_callback_query(filters.regex("cbsetting"))
async def cbsetting(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ᴘᴀᴠᴀɴ ꜱᴇᴛᴛɪɴɢꜱ ᴄᴏᴍᴍᴀɴᴅꜱ :**

» /pause - ꜰᴏʀ ᴘᴀᴜꜱɪɴɢ ꜱᴛʀᴇᴀᴍɪɴɢ. 
» /resume - ꜰᴏʀ ʀᴇꜱᴜᴍᴇ ꜱᴛʀᴇᴀᴍɪɴɢ. 
» /skip - ꜰᴏʀ ꜱᴋɪᴘᴘɪɴɢ ᴄᴜʀʀᴇɴᴛ ꜱᴏɴɢ ᴀɴᴅ ᴘʟᴀʏɪɴɢ ɴᴇxᴛ ꜱᴏɴɢ. 
» /mute - ꜰᴏʀ ᴍᴜᴛᴜɪɴɢ ᴀꜱꜱɪꜱᴛᴀɴᴛ ɪɴ ᴠᴄ. 
» /unmute - ꜰᴏʀ ᴜɴᴍᴜᴛᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛ ɪɴ ᴠᴄ. 
» /end - ꜰᴏʀ ᴇɴᴅ ꜱᴛʀᴇᴀᴍɪɴɢ. 

**© @TheCreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="cbcmds")]]
        ),
    )
@app.on_message(filters.new_chat_members, group=welcome_captcha_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    for member in message.new_chat_members:
        try:
            if member.id in OWNER:
                return await message.reply_text(
                    f"💡 Pemilik Bot [{member.mention}] baru saja bergabung di grup ini."
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    f"💡 Admin Bot [{member.mention}] baru saja bergabung di grup ini."
                )
            if member.id == ASSID:
                await remove_active_chat(chat_id)
            if member.id == BOT_ID:
                out = start_pannel()
                await message.reply_text(
                    f"""
👋 ** Halo senang rasanya bisa bergabung di grup ini**

💡 **Jangan lupa untuk menjadikan saya sebagai admin di grup ini**
""",
                    reply_markup=InlineKeyboardMarkup(out[1]),
                    disable_web_page_preview=True
                )
                return
        except BaseException:
            return


@Client.on_message(
    filters.group
    & filters.command(
        ["start", "help", f"start@{BOT_USERNAME}", f"help@{BOT_USERNAME}"]
    )
)
async def start(_, message: Message):
    chat_id = message.chat.id
    out = start_pannel()
    await message.reply_text(
        f"""
Terima kasih telah memasukkan saya di {message.chat.title}.
Musik itu hidup.

Untuk bantuan silahkan klik tombol dibawah.
""",
        reply_markup=InlineKeyboardMarkup(out[1]),
        disable_web_page_preview=True
    )
    return


@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def play(_, message: Message):
    if len(message.command) == 1:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        await app.send_message(
            message.chat.id,
            text=f"""
**✨ Selamat Datang {rpk}!

💬 [{BOT_NAME}](tg://user?id=2129034376) memungkinkan anda untuk memutar musik pada grup melalui obrolan suara yang baru di Telegram!

💡 Untuk Mengetahui Semua Perintah Bot Dan Bagaimana Cara Kerja Nya Dengan Menekan Tombol » 📚 ᴄᴏᴍᴍᴀɴᴅ​!**

""",
            parse_mode="markdown",
            reply_markup=pstart_markup,
            reply_to_message_id=message.message_id,
        )
    elif len(message.command) == 2:
        query = message.text.split(None, 1)[1]
        f1 = query[0]
        f2 = query[1]
        f3 = query[2]
        finxx = f"{f1}{f2}{f3}"
        if str(finxx) == "inf":
            query = (str(query)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
                x = ytdl.extract_info(query, download=False)
            thumbnail = x["thumbnail"]
            searched_text = f"""
🔍 **Video Track Information**

❇️**Judul:** {x["title"]}

⏳ **Durasi:** {round(x["duration"] / 60)} Mins
👀 **Ditonton:** `{x["view_count"]}`
👍 **Suka:** `{x["like_count"]}`
👎 **Tidak suka:** `{x["dislike_count"]}`
⭐️ **Peringkat Rata-rata:** {x["average_rating"]}
🎥 **Nama channel:** {x["uploader"]}
📎 **Channel Link:** [Kunjungi Dari Sini]({x["channel_url"]})
🔗 **Link:** [Link]({x["webpage_url"]})
"""
            link = x["webpage_url"]
            buttons = personal_markup(link)
            userid = message.from_user.id
            thumb = await down_thumb(thumbnail, userid)
            await app.send_photo(
                message.chat.id,
                photo=thumb,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if str(finxx) == "sud":
            sudoers = await get_sudoers()
            text = "**📝 DAFTAR PENGGUNA SUDO**\n\n"
            for count, user_id in enumerate(sudoers, 1):
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name if not user.mention else user.mention
                except Exception:
                    continue
                text += f"- {user}\n"
            if not text:
                await message.reply_text("Tidak Ada Pengguna Sudo")
            else:
                await message.reply_text(text)


@app.on_message(filters.command("settings") & filters.group)
async def settings(_, message: Message):
    c_id = message.chat.id
    _check = await get_assistant(c_id, "assistant")
    if not _check:
        assis = {
            "volume": 100,
        }
        await save_assistant(c_id, "assistant", assis)
        volume = 100
    else:
        volume = _check["volume"]
    text, buttons = setting_markup()
    await asyncio.gather(
        message.delete(),
        message.reply_text(f"{text}\n\n**Group:** {message.chat.title}\n**Group ID:** {message.chat.id}\n**Volume Level:** {volume}%", reply_markup=InlineKeyboardMarkup(buttons)),
    )

@app.on_callback_query(filters.regex("okaybhai"))
async def okaybhai(_, CallbackQuery):
    await CallbackQuery.answer("Going Back ...")
    out = start_pannel()
    await CallbackQuery.edit_message_text(
        text=f"Terimakasih telah menambahkan saya di {CallbackQuery.message.chat.title}.\n{BOT_NAME} Telah online.\n\nJika butuh bantuan atau terjadi masalah dengan Bot silahkan bergabung di group atau channel kami.",
        reply_markup=InlineKeyboardMarkup(out[1]),
    )

@app.on_callback_query(filters.regex("settingm"))
async def settingm(_, CallbackQuery):
    await CallbackQuery.answer("Bot Settings ...")
    text, buttons = setting_markup()
    c_title = CallbackQuery.message.chat.title
    c_id = CallbackQuery.message.chat.id
    chat_id = CallbackQuery.message.chat.id
    _check = await get_assistant(c_id, "assistant")
    if not _check:
        assis = {
            "volume": 100,
        }
        await save_assistant(c_id, "assistant", assis)
        volume = 100
    else:
        volume = _check["volume"]
    await CallbackQuery.edit_message_text(
        text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%",
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@app.on_callback_query(filters.regex("EVE"))
@ActualAdminCB
async def EVE(_, CallbackQuery):
    checking = CallbackQuery.from_user.username
    text, buttons = usermarkup()
    chat_id = CallbackQuery.message.chat.id
    is_non_admin = await is_nonadmin_chat(chat_id)
    if not is_non_admin:
        await CallbackQuery.answer("Changes Saved")
        await add_nonadmin_chat(chat_id)
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\nAdmins Commands Mode to **Everyone**\n\nNow anyone present in this group can skip, pause, resume, stop music.\n\nChanges Done By @{checking}",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        await CallbackQuery.answer(
            "Commands Mode is Already Set To EVERYONE", show_alert=True
        )

@app.on_callback_query(filters.regex("AMS"))
@ActualAdminCB
async def AMS(_, CallbackQuery):
    checking = CallbackQuery.from_user.username
    text, buttons = usermarkup()
    chat_id = CallbackQuery.message.chat.id
    is_non_admin = await is_nonadmin_chat(chat_id)
    if not is_non_admin:
        await CallbackQuery.answer(
            "Commands Mode is Already Set To ADMINS ONLY", show_alert=True
        )
    else:
        await CallbackQuery.answer("Changes Saved")
        await remove_nonadmin_chat(chat_id)
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\nSet Commands Mode to **Admins**\n\nNow only Admins present in this group can skip, pause, resume, stop musics.\n\nChanges Done By @{checking}",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@app.on_callback_query(
    filters.regex(
        pattern=r"^(AQ|AV|AU|Dashboard|HV|LV|MV|HV|VAM|Custommarkup|PTEN|MTEN|PTF|MTF|PFZ|MFZ|USERLIST|UPT|CPT|RAT|DIT)$"
    )
)
async def start_markup_check(_, CallbackQuery):
    command = CallbackQuery.matches[0].group(1)
    c_title = CallbackQuery.message.chat.title
    c_id = CallbackQuery.message.chat.id
    chat_id = CallbackQuery.message.chat.id
    if command == "AQ":
        await CallbackQuery.answer("Already in Best Quality", show_alert=True)
    if command == "AV":
        await CallbackQuery.answer("Bot Settings ...")
        text, buttons = volmarkup()
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "AU":
        await CallbackQuery.answer("Bot Settings ...")
        text, buttons = usermarkup()
        is_non_admin = await is_nonadmin_chat(chat_id)
        if not is_non_admin:
            current = "Admins Only"
        else:
            current = "Everyone"
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n\nCurrently Who Can Use {BOT_NAME}:- **{current}**\n\n**⁉️ What is This?**\n\n**👥 Everyone :-**Anyone can use {BOT_NAME}'s commands(skip, pause, resume etc) present in this group.\n\n**🙍 Admin Only :-**  Only the admins and authorized users can use all commands of {BOT_NAME}.",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "Dashboard":
        await CallbackQuery.answer("Dashboard...")
        text, buttons = dashmarkup()
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n\nCheck {BOT_NAME}'s System Stats In the DashBoard Here! More Functions adding very soon! Keep on Checking Support Channel.",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "Custommarkup":
        await CallbackQuery.answer("Bot Settings ...")
        text, buttons = custommarkup()
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "LV":
        assis = {
            "volume": 25,
        }
        volume = 25
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MV":
        assis = {
            "volume": 50,
        }
        volume = 50
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "HV":
        assis = {
            "volume": 100,
        }
        volume = 100
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "VAM":
        assis = {
            "volume": 200,
        }
        volume = 200
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "PTEN":
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        volume = volume + 10
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MTEN":
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        volume = volume - 10
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "PTF":
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        volume = volume + 25
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MTF":
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        volume = volume - 25
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "PFZ":
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        volume = volume + 50
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MFZ":
        _check = await get_assistant(c_id, "assistant")
        volume = _check["volume"]
        volume = volume - 50
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("Setting Audio Changes ...")
        except:
            return await CallbackQuery.answer("No active Group Call...")
        await save_assistant(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**Group:** {c_title}\n**Group ID:** {c_id}\n**Volume Level:** {volume}%\n**Audio Quality:** Default Best",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "USERLIST":
        await CallbackQuery.answer("Auth Users!")
        text, buttons = usermarkup()
        _playlist = await get_authuser_names(CallbackQuery.message.chat.id)
        if not _playlist:
            return await CallbackQuery.edit_message_text(
                text=f"{text}\n\nNo Authorized Users Found\n\nYou can allow any non-admin to use my admin commands by /auth and delete by using /unauth",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        else:
            j = 0
            await CallbackQuery.edit_message_text(
                "Fetching Authorised Users... Please Wait"
            )
            msg = f"**Authorised Users List[AUL]:**\n\n"
            for note in _playlist:
                _note = await get_authuser(
                    CallbackQuery.message.chat.id, note
                )
                user_id = _note["auth_user_id"]
                user_name = _note["auth_name"]
                admin_id = _note["admin_id"]
                admin_name = _note["admin_name"]
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name
                    j += 1
                except Exception:
                    continue
                msg += f"{j}➤ {user}[`{user_id}`]\n"
                msg += f"    ┗ Added By:- {admin_name}[`{admin_id}`]\n\n"
            await CallbackQuery.edit_message_text(
                msg, reply_markup=InlineKeyboardMarkup(buttons)
            )
    if command == "UPT":
        bot_uptimee = int(time.time() - bot_start_time)
        Uptimeee = f"{get_readable_time((bot_uptimee))}"
        await CallbackQuery.answer(
            f"Bot's Uptime: {Uptimeee}", show_alert=True
        )
    if command == "CPT":
        cpue = psutil.cpu_percent(interval=0.5)
        await CallbackQuery.answer(
            f"Bot's Cpu Usage: {cpue}%", show_alert=True
        )
    if command == "RAT":
        meme = psutil.virtual_memory().percent
        await CallbackQuery.answer(
            f"Bot's Memory Usage: {meme}%", show_alert=True
        )
    if command == "DIT":
        diske = psutil.disk_usage("/").percent
        await CallbackQuery.answer(
            f"Disk Usage: {diske}%", show_alert=True
        )
