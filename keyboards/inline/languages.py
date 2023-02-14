from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="👍uz"),
            InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data="👍ru"),
        ],
        [
            InlineKeyboardButton(text="🇬🇧 Ingliz tili", callback_data="👍en"),
            InlineKeyboardButton(text="🇸🇦 Arab tili", callback_data="👍ar"),
        ],
        [
            InlineKeyboardButton(text="🇰🇷 Kores tili", callback_data="👍kr"),
            InlineKeyboardButton(text="🇨🇳 Xitoy tili", callback_data="👍zh"),
        ],
        [
            InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel"),
        ]

    ]

)

button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="👍uz"),
            InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data="👍ru"),
        ],
        [
            InlineKeyboardButton(text="🇬🇧 Ingliz tili", callback_data="👍en"),
            InlineKeyboardButton(text="🇸🇦 Arab tili", callback_data="👍ar"),
        ],
        [
            InlineKeyboardButton(text="🇰🇷 Kores tili", callback_data="👍ko"),
            InlineKeyboardButton(text="🇨🇳 Xitoy tili", callback_data="👍zh-CN"),
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="back"),
        ]

    ]

)