from fastapi import FastAPI

from aiogram import Bot, Dispatcher, types

from bot import bot, dispatcher, register_all_handlers
from config import WEBHOOK_URL, WEBHOOK_PATH

import urllib.request

app = FastAPI()

register_all_handlers()


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL,
            allowed_updates=False
        )
    print(webhook_info)
    pass


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dispatcher)
    Bot.set_current(bot)
    await dispatcher.process_update(telegram_update)


@app.on_event("shutdown")
async def api_on_startup():
    print("API shutdown")
    pass
