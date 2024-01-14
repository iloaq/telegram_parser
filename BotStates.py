from aiogram.dispatcher.filters.state import State, StatesGroup


class StorageStates(StatesGroup):
    loading_links_base = State()
    parsing = State()


class StatesNames:
    loading_links_base = "loading_links_base"
    parsing = "parsing"
