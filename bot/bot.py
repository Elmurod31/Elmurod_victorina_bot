import asyncio
from os import getenv
import os
from aiogram import Dispatcher, Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, Message
from dotenv import load_dotenv

from hadlers import handlers_router
from keyboard import add_btn
load_dotenv()
dp = Dispatcher()
TOKEN = getenv("TOKEN")

router = Router()


dp.include_router(handlers_router)

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path)
    full_name = f"{message.from_user.first_name} {message.from_user.last_name}"
    await message.answer_photo(img, caption=f"Hush kelibsiz {full_name} blag'on sizga nechta savollar berib bilimingizni tekshirib beramiz! 😊", reply_markup=add_btn)

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot starting....")
    asyncio.run(main())