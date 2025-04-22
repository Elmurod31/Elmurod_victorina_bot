import os
import random

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from keyboard import add_btn, add_btns

handlers_router = Router()



@handlers_router.message(CommandStart())
async def command_start_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path)
    full_name = f"{message.from_user.first_name} {message.from_user.last_name}"
    await message.answer_photo(img, caption=f"Hush kelibsiz {full_name} blag'on sizga nechta savollar berib bilimingizni tekshirib beramiz! 😊", reply_markup=add_btn)


@handlers_router.message(F.text == "LEVEL1️⃣")
async def level_1(message: Message):
    question = (f"{random.randint(1, 11)} {random.choice(['+', '-', '*'])} {random.randint(1, 10)}")
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)


@handlers_router.message(F.text == "LEVEL2️⃣")
async def level_1(message: Message):
    question = (f"{random.randint(11, 111)} {random.choice(['+', '-', '*'])} {random.randint(10, 100)}")
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)


@handlers_router.message(F.text == "LEVEL3️⃣")
async def level_1(message: Message):
    question = (f"{random.randint(111, 1111)} {random.choice(['+', '-', '*', ':'])} {random.randint(100, 1000)}")
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)


@handlers_router.message(F.text == "LEVEL4️⃣")
async def level_1(message: Message):
    question = (f"{random.randint(1111, 11111111)} {random.choice(['+', '-', '*', ':'])} {random.randint(1000, 1000000)}")
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)


@handlers_router.message(F.text == "Stop⛔")
async def command_start_handler(message: Message):
    await message.answer(text="Stop⛔ ", reply_markup=add_btn),

