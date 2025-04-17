from aiogram.fsm.state import StatesGroup, State

class LevelState(StatesGroup):
    level = State()
    answer = State()