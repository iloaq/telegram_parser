from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

import keyboards
import helpers
from commands import CommandsNames


async def break_operation(message: types.Message, state: FSMContext):
    if not helpers.is_valid_id(message):
        return

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()

    await message.answer("Операция отменена", reply_markup=keyboards.main_menu_keyboard())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(break_operation, text=CommandsNames.BREAK_OPERATION_COMMAND, state="*")
