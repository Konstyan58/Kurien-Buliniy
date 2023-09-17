from aiogram import types, Dispatcher
from config import bot
from settings import ADMINS


async def send_welcome(message: types.Message):
    await bot.send_message(ADMINS[0], '😉')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['something'])
