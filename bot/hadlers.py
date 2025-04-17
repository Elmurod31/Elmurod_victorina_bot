import random

from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from bot.states import LevelState

handlers_router = Router()

@handlers_router.message(LevelState.level)
async def lvl_handler(message: types.Message, state: FSMContext):
    if message.text == "LEVEL1️⃣":
        question = f"{random.randrange(1, 11)} {random.choice(['+', '-', '*'])} {random.randrange(1, 11)}"
        answer = eval(question)
        await state.update_data(answer=answer, level=message.text, true=0, false=0)
        await message.answer(f"SAVOL : {question} = ?")
        await state.set_state(LevelState.answer)
