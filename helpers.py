from aiogram import types
import config


def is_valid_id(message: types.Message):
    if message.chat.id == config.ADMIN_ID:
        return True
    else:
        return False
