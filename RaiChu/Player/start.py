
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**I แดแด ๐๐๐๐ใป๐ฝ๐๐
สแดแด สแดษดแดสแด สส [๐๐๐๐ใป๐ผ๐๐๐](https://t.me/lgcyalex)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐พ๐ค๐ฃ๐ฉ๐๐๐ฉ ๐๐", url="https://t.me/lgcyalex"
                    ),
                    InlineKeyboardButton(
                        "๐พ๐ค๐ข๐ข๐๐ฃ๐ ๐๐๐จ๐ฉ๐ ", url="https://telegra.ph/%C5%81GcYA%C5%81EX-02-18"
                    )
                  ],[
                    InlineKeyboardButton(
                       "๐๐ค๐๐ฃ ๐๐ง๐ค๐ช๐ฅ", url="https://t.me/LGCY_OFFICIAL"
                    ),
                    InlineKeyboardButton(
                        "๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ", url="https://t.me/Clan8Xofficial"
                    )
                ],[
                    InlineKeyboardButton(
                        "โ ๐๐๐ ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉโ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
