from aiogram.dispatcher.filters.state import StatesGroup, State

class Translator(StatesGroup):
    inp = State()
    out = State()
    text = State()