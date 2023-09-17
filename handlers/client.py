from aiogram import types, Dispatcher
from config import bot


async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, '')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
