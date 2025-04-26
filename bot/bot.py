import asyncio
import menu
from os import getenv
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from hadlers import handlers_router

from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy="https://proxy.server:3128")

load_dotenv()
dp = Dispatcher()
TOKEN = getenv("TOKEN")



dp.include_router(handlers_router)



async def main() -> None:
    bot = Bot(token=TOKEN, session=session)
    await menu.set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot starting.....")
    asyncio.run(main())