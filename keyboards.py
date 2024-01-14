from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from commands import CommandsNames


def break_operation_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(CommandsNames.BREAK_OPERATION_COMMAND))

    return keyboard


def break_parsing_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(CommandsNames.BREAK_PARSING))

    return keyboard


def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(CommandsNames.START_PARSING))
    keyboard.add(KeyboardButton(CommandsNames.LOAD_LINKS))

    return keyboard