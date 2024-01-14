from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import BOT_API_TOKEN
from commands import StartCommand, LoadLinksCommand, BreakOperationCommand, ParsingCommand


class StorageNames:
    load_links = "load_links"


storage = MemoryStorage()

bot = Bot(BOT_API_TOKEN)
dispatcher = Dispatcher(bot, storage=storage)

CREATE_LINK_COMMAND = "🆕 Создать ссылку"

DEFAULT_KEYBOARD = ReplyKeyboardMarkup(resize_keyboard=True)
DEFAULT_KEYBOARD.add(KeyboardButton(CREATE_LINK_COMMAND))


def register_all_handlers():
    BreakOperationCommand.register_handlers(dispatcher)

    StartCommand.register_handlers(dispatcher)
    LoadLinksCommand.register_handlers(dispatcher)

    ParsingCommand.register_handlers(dispatcher)