from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Music import BOT_NAME
from Music.config import GROUP, CHANNEL

def play_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumevc2"),
            InlineKeyboardButton(text="II", callback_data=f"pausevc2"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipvc2"),
            InlineKeyboardButton(text="▢", callback_data=f"stopvc2"),
        ],[
            InlineKeyboardButton(text="⇩ ɢᴇᴛ ᴀᴜᴅɪᴏ​​", callback_data=f"gets audio|{videoid}|{user_id}"),
            InlineKeyboardButton(text="⇩ ɢᴇᴛ ᴠɪᴅᴇᴏ", callback_data=f"gets video|{videoid}|{user_id}"),
        ],
        [      
            InlineKeyboardButton(text="≡ ᴍᴇɴᴜ", callback_data=f"other {videoid}|{user_id}"),   
            InlineKeyboardButton(text="↺ ᴄʟᴏꜱᴇ", callback_data=f"close"),
        ],
    ]
    return buttons


def others_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumevc2"),
            InlineKeyboardButton(text="II", callback_data=f"pausevc2"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipvc2"),
            InlineKeyboardButton(text="▢", callback_data=f"stopvc2"),
        ],
        [
            InlineKeyboardButton(text="➕ ᴀᴅᴅ ᴜʀ ʟɪsᴛ​", callback_data=f'playlist {videoid}|{user_id}'),
            InlineKeyboardButton(text="➕ ᴀᴅᴅ ɢʀᴘ ʟɪsᴛ​", callback_data=f'group_playlist {videoid}|{user_id}'),
        ],
        [
            InlineKeyboardButton(
                text="⇩ ɢᴇᴛ ᴀᴜᴅɪᴏ", callback_data=f"gets audio|{videoid}|{user_id}"
            ),
            InlineKeyboardButton(
                text="⇩ ɢᴇᴛ ᴠɪᴅᴇᴏ", callback_data=f"gets video|{videoid}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⌫", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="ᴄʟᴏꜱᴇ", callback_data=f"close2"),
        ],
    ]
    return buttons


play_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("▷", callback_data="resumevc"),
            InlineKeyboardButton("II", callback_data="pausevc"),
            InlineKeyboardButton("‣‣I", callback_data="skipvc"),
            InlineKeyboardButton("▢", callback_data="stopvc"),
        ],
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")],
    ]
)


def audio_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumevc2"),
            InlineKeyboardButton(text="II", callback_data=f"pausevc2"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipvc2"),
            InlineKeyboardButton(text="▢", callback_data=f"stopvc2"),
        ],
        [InlineKeyboardButton(text="ᴄʟᴏꜱᴇ", callback_data="close2")],
    ]
    return buttons


def search_markup(
    ID1,
    duration1,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴄᴏɴꜰɪʀᴍ", callback_data=f"Music2 {ID1}|{duration1}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴄᴀɴᴄᴇʟ", callback_data=f"ppcl2 smex|{user_id}"
            ),
        ],
    ]
    return buttons


def personal_markup(link):
    buttons = [
        [InlineKeyboardButton(text="ᴛᴏɴᴛᴏɴ ᴅɪ ʏᴏᴜᴛᴜʙᴇ", url=f"{link}")],
        [InlineKeyboardButton(text="ᴄʟᴏꜱᴇ", callback_data=f"close2")],
    ]
    return buttons


start_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "📚 ᴅᴀꜰᴛᴀʀ ᴘᴇʀɪɴᴛᴀʜ​ 📚", url="https://telegra.ph/ҡʏʏ-ᴇx-12-15"
            )
        ],
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close2")],
    ]
)

confirm_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ʏᴀ", callback_data="cbdel"),
            InlineKeyboardButton("ᴛɪᴅᴀᴋ", callback_data="close2"),
        ]
    ]
)

confirm_group_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ʏᴀ", callback_data="cbgroupdel"),
            InlineKeyboardButton("ᴛɪᴅᴀᴋ", callback_data="close2"),
        ]
    ]
)

close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close2")]]
)

play_list_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "➕ ᴜsᴇʀ ᴘʟᴀʏʟɪsᴛ​", callback_data="P_list"
                    ),
                    InlineKeyboardButton(
                        "➕ ɢʀᴏᴜᴘ ᴘʟᴀʏʟɪsᴛ​​", callback_data="G_list"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴄʟᴏꜱᴇ", callback_data="close2"
                    )
                ]
            ]
        )

def playlist_markup(user_name, user_id):
    buttons= [
            [
                InlineKeyboardButton(text=f"ɢʀᴏᴜᴘs", callback_data=f'play_playlist {user_id}|group'),
            ],
            [
                InlineKeyboardButton(text=f"{user_name[:8]}", callback_data=f'play_playlist {user_id}|personal'),
            ],
            [
                InlineKeyboardButton(text="ᴄʟᴏꜱᴇ", callback_data="close2")              
            ],
        ]
    return buttons


def start_pannel():
    if not CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons
    if not CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="✨ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons


def private_panel():
    if not CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons
    if not CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴏs",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {BOT_NAME}*", buttons
    if CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons
    if CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="✨ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 ᴀᴜᴅɪᴏ ǫᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 ᴅᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 ʀᴇsᴇᴛ ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 ʟᴏᴡ ᴠᴏʟ", callback_data="LV"),
            InlineKeyboardButton(text="🔉 ᴍᴇᴅɪᴜᴍ ᴠᴏʟ", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 ʜɪɢʜ ᴠᴏʟ", callback_data="HV"),
            InlineKeyboardButton(text="🔈 ᴀᴍᴘʟɪғɪᴇᴅ ᴠᴏʟ", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 ᴄᴜsᴛᴏᴍ ᴠᴏʟᴜᴍᴇ 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 ᴄᴜsᴛᴏᴍ ᴠᴏʟᴜᴍᴇ 🔼", callback_data="AV")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 ᴇᴠʀʏᴏɴᴇ", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 ᴀᴅᴍɪɴs", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀ ʟɪsᴛ", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ ᴜᴘᴛɪᴍᴇ", callback_data="UPT"),
            InlineKeyboardButton(text="💾 ʀᴀᴍ", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 ᴄᴘᴜ", callback_data="CPT"),
            InlineKeyboardButton(text="💽 ᴅɪsᴋ", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="sᴛᴏʀᴀɢᴇ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="sᴛᴏʀᴀɢᴇ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),            
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="sᴛᴏʀᴀɢᴇ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)


stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴏᴛ sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ɢᴇᴛᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
