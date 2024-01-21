from aiogram import types, Dispatcher
from config import bot
from settings import ADMINS
from keyboards.admin_inline import buttons_for_admin
from handler_db import Database
from aiogram.utils.exceptions import ChatNotFound

database = Database(pute_k_fily="datas_base/file_dla_chelovekov.db")


async def send_welcome(message: types.Message):
    prinimanie_buttons = buttons_for_admin()
    await bot.send_message(ADMINS[0], 'дарова', reply_markup=prinimanie_buttons)
    # await bot.send_poll(ADMINS[0], 'было 2 козла, сколько?',
    #                     options=['это загадка от Жака Фреско', 'ъуъ'],
    #                     open_period=10,
    #                     explanation='а хрен его знает',
    #                     correct_option_id=1,
    #                     type='quiz')


async def BAN(message: types.Message):
    if message.from_user.id == 6274719470:
        nick = message.text.split()
        idyshick_cheloveka = nick[1]
        prichina_bana = " ".join(nick[2:])
        first_or_last_nm = "Фёдор Беликов"
        usr_nm = "Фёдор228"
        await database.add_client_for_ban(nedo_id=idyshick_cheloveka, frst_or_lst_name=first_or_last_nm,
                                          username=usr_nm, prichina=prichina_bana)
        try:
            await bot.send_message(idyshick_cheloveka, text="Вы забанены, если есть вопросы пишите: @The_Steve8")
        except ChatNotFound:
            await bot.send_message(message.from_user.id,
                                   'ОШИБКА СТОП ERROR 404!!!1111!! ТАКОГО ЧЕБУРЕКА НЕ НАЙДЕНО!!11!!1')
    else:
        await bot.send_message(message.from_user.id, 'чел... ты не админ, ты не можешь банить')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['something.py', 's', 'qest'])
    dp.register_message_handler(BAN, commands=['ban'])
