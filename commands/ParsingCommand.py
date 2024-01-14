import asyncio
import urllib.request
from datetime import datetime

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

import config
import keyboards
import helpers

from commands import CommandsNames
from BotStates import StorageStates

import time


async def parsing_command(message: types.Message):
    if not helpers.is_valid_id(message):
        return

    if len(config.PARSE_LINKS) == 0:
        await message.answer("Нет загруженных ссылок", reply_markup=keyboards.main_menu_keyboard())
        return

    config.ALREADY_PARSING = True

    await StorageStates.parsing.set()
    await message.answer("Начался перебор", reply_markup=keyboards.break_parsing_keyboard())

    opener = urllib.request.FancyURLopener({})
    while config.ALREADY_PARSING:
        start_time = time.time()

        iteration = 0
        fullCount = len(config.PARSE_LINKS)

        for link in config.PARSE_LINKS:
            # print(f'iteration {iteration} | {fullCount}')
            iteration += 1
            try:
                f = opener.open(link)
                content = f.read()

                if "<meta name=\"robots\" content=\"noindex, nofollow\">" in str(content.decode('utf-8')):
                    await message.answer(f"Нерабочая ссылка: {link}")

                if not config.ALREADY_PARSING:
                    return
            except:
                pass

        stop_time = time.time()
        print(f"Перебор закончился. {datetime.fromtimestamp(start_time)} | {datetime.fromtimestamp(stop_time)}")

    await asyncio.sleep(10)


async def break_parsing(message: types.Message, state: FSMContext):
    if not helpers.is_valid_id(message):
        return

    config.ALREADY_PARSING = False

    await message.answer("Перебор остановлен", reply_markup=keyboards.main_menu_keyboard())

    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(parsing_command, text=CommandsNames.START_PARSING, state=None)
    dp.register_message_handler(break_parsing, text=CommandsNames.BREAK_PARSING, state=StorageStates.parsing)
