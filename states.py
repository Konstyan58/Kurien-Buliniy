from aiogram.dispatcher.filters.state import State, StatesGroup


class StateIdea(StatesGroup):
    wait_to_idea = State()
