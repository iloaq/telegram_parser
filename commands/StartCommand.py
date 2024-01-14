from aiogram import Dispatcher, types

import keyboards
import helpers
from commands import CommandsNames


async def command_start(message: types.Message):
    if not helpers.is_valid_id(message):
        return

    await message.answer("Готов к работе", reply_markup=keyboards.main_menu_keyboard())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=CommandsNames.START_COMMAND)
