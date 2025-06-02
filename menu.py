# Bot menyusiga buyruqlarni o'rnatish funksiyasi
from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Bot haqida yordam"),
    ]
    await bot.set_my_commands(commands)