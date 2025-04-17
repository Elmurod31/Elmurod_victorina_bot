from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

add_btn = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="LEVEL1️⃣"),
        KeyboardButton(text="LEVEL2️⃣")
    ],
    [
        KeyboardButton(text="LEVEL3️⃣"),
        KeyboardButton(text="LEVEL4️⃣")
    ]
], resize_keyboard=True)