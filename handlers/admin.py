from aiogram import types, Dispatcher
from config import bot
from settings import ADMINS
from keyboards.admin_inline import buttons_for_admin


async def send_welcome(message: types.Message):
    prinimanie_buttons = buttons_for_admin()
    await bot.send_message(ADMINS[0], 'дарова', reply_markup=prinimanie_buttons)
    # await bot.send_poll(ADMINS[0], 'было 2 козла, сколько?',
    #                     options=['это загадка от Жака Фреско', 'ъуъ'],
    #                     open_period=10,
    #                     explanation='а хрен его знает',
    #                     correct_option_id=1,
    #                     type='quiz')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['something.py', 's', 'qest'])
