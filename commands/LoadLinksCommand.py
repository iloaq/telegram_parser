from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

import keyboards
import helpers
from commands import CommandsNames

from BotStates import StorageStates, StatesNames

import config


async def start_load_links(message: types.Message):
    if not helpers.is_valid_id(message):
        return

    await StorageStates.loading_links_base.set()
    await message.answer("Отправь файл с расширением .txt", reply_markup=keyboards.break_operation_keyboard())


async def loading_links(message: types.Message, state: FSMContext):
    if not helpers.is_valid_id(message):
        return

    save_file_info = await message.document.download()
    file_name = save_file_info.name
    with open(file_name) as f:
        config.PARSE_LINKS = f.readlines()

    await state.finish()
    await message.answer(f"Загружено {len(config.PARSE_LINKS)} ссылок", reply_markup=keyboards.main_menu_keyboard())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_load_links, text=CommandsNames.LOAD_LINKS, state=None)
    dp.register_message_handler(loading_links, content_types=['document'], state=StorageStates.loading_links_base)
