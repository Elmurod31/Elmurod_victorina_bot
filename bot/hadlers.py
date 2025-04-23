import os
import random

from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from states import LevelState
from keyboard import add_btn, add_btns

handlers_router = Router()

def get_min_max_number(level):
    if level == "LEVEL1️⃣":
        return 1, 11
    elif level == "LEVEL2️⃣":
        return 11, 111
    elif level == "LEVEL3️⃣":
        return 111, 1111
    else:
        return 1111, 11111111

@handlers_router.message(CommandStart())
async def command_start_handler(message: Message):
    img_path = os.path.join(os.path.dirname(__file__), "images", "img.png")
    img = FSInputFile(img_path)
    full_name = f"{message.from_user.first_name} {message.from_user.last_name}"
    await message.answer_photo(img, caption=f"Hush kelibsiz {full_name} blag'on sizga nechta savollar berib bilimingizni tekshirib beramiz! 😊", reply_markup=add_btn)


@handlers_router.message(F.text == "LEVEL1️⃣")
async def level_1(message: Message, state: FSMContext):
    question = f"{random.randint(1, 11)} {random.choice(['+', '-', '*'])} {random.randint(1, 10)}"
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL1️⃣", correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)
    await state.set_state(LevelState.javob)




@handlers_router.message(F.text == "LEVEL2️⃣")
async def level_2(message: Message, state: FSMContext):
    question = f"{random.randint(11, 111)} {random.choice(['+', '-', '*'])} {random.randint(10, 100)}"
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL1️⃣", correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)
    await state.set_state(LevelState.javob)


@handlers_router.message(F.text == "LEVEL3️⃣")
async def level_3(message: Message, state: FSMContext):
    question = f"{random.randint(111, 1111)} {random.choice(['+', '-', '*', ':'])} {random.randint(100, 1000)}"
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL33️⃣", correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)
    await state.set_state(LevelState.javob)


@handlers_router.message(F.text == "LEVEL4️⃣")
async def level_4(message: Message, state: FSMContext):
    question = f"{random.randint(1111, 11111111)} {random.choice(['+', '-', '*', ':'])} {random.randint(1000, 1000000)}"
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="LEVEL4️⃣", correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)
    await state.set_state(LevelState.javob)


@handlers_router.message(F.text == "Stop⛔")
async def command_stop_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    correct = data.get("correct", 0)
    incorrect = data.get("incorrect", 0)
    level = data.get("level", 0)

    total = correct + incorrect

    await message.answer(
        text=f"Stop⛔\n"
             f"Savollar soni: {total}\n"
             f"✅ To'g'ri javoblar: {correct}\n"
             f"❌ Noto‘g‘ri javoblar: {incorrect}",
        reply_markup=add_btn
    )


@handlers_router.message(StateFilter(LevelState.javob))
async def process(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    correct_answer = data.get("answer")
    correct = data.get("correct", 0)
    incorrect = data.get("incorrect", 0)
    level = data.get("level")
    print(correct_answer)
    try:
        user_answer = int(message.text)
        if user_answer == correct_answer:
            correct += 1
            await message.answer("Javob tog'ri")
        else:
            incorrect += 1
            await message.answer("Javob notog'ri")
    except ValueError:
        await message.answer("Iltimos raqam kiriting")

    min_number, max_number = get_min_max_number(level)
    question = (f"{random.randint(min_number, max_number)}"
                f"{random.choice(['+', '-', '*'])}"
                f"{random.randint(min_number, max_number)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, correct=correct, incorrect=incorrect)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=add_btns)