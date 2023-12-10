from aiogram import types, Dispatcher
from config import bot
from keyboards.client_inline import buttons_for_menu, buttons_for_svaz
from pprint import pprint
import requests
from settings import API_TOKEN
from utils.text_utils import s
from handler_db import Database
import random

database = Database(pute_k_fily="datas_base/file_dla_chelovekov.db")
photos = ['imgs/1696502279_gas-kvas-com-p-kartinki-lyubie-27.jpg',
          'imgs/a253c5869732a1cbabf74443e1467efd.jpeg',
          'imgs/1e0783c1571e76f71b9bdf2308ffe308.jpeg']
file_idys=['AgACAgIAAxkBAAIDHWVzDFFRtiGVbnhqJlCq1ExWs-_nAAKjzjEbyEaYSw8NyTtb9MVAAQADAgADeQADMwQ',
           'AgACAgIAAxkBAAIDHmVzDGGG5CN7HNlYzuIfcocgwUHSAAKkzjEbyEaYS1NdHxYrzrnzAQADAgADeQADMwQ',
           'AgACAgIAAxkBAAIDH2VzDG4DK0om553HTUnSu6GBT4srAAKlzjEbyEaYS_zFTGyeVF_cAQADAgADeQADMwQ']


async def send_locate(message: types.Message):
    cntry, ppltn, temp, vlsnst = s(message.location.latitude, message.location.longitude, API_TOKEN)

    latitude = message.location.latitude
    longituide = message.location.longitude
    await bot.send_message(message.from_user.id, f'Ваши координаты {latitude},{longituide} \n'
                                                 f'Ваша страна (хотя если пользуетесь этим ботом то живёте в СНГ, если конечно бота не перевели): {cntry} \n'
                                                 f'Ваша температура {temp} \n'
                                                 f'Влажность {vlsnst} \n'
                                                 f'AQI {ppltn}')

async def message_text(message: types.Message):
        file_iydishnik=message.photo[-1].file_id
        print(file_iydishnik)
        await message.photo[-1].download('img/am.jpg')

async def send_welcome(message: types.Message):
    # await database.crt_new_tbl()
    await database.add_client(nedo_id=message.from_user.id,
                              frst_or_lst_name=f"{message.from_user.first_name}, {message.from_user.last_name}",
                              username=message.from_user.username)
    await bot.delete_message(message.from_user.id, message.message_id)

    print(message)
    prinimanie_buttons = buttons_for_menu()
    await bot.send_photo(message.from_user.id, random.choice(file_idys), caption='шото не знаю шо', has_spoiler=False,
                         reply_markup=prinimanie_buttons)

async def func(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    prinimanie_buttons = buttons_for_svaz()
    await bot.send_photo(callback.from_user.id, random.choice(file_idys), caption='шото не знаю шо', has_spoiler=False,
                         reply_markup=prinimanie_buttons)
async def send_something(callback: types.CallbackQuery):
    print(callback)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(message_text, content_types=['photo'])
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_callback_query_handler(send_something, lambda s: s.data == "CLICK_ME")
    dp.register_callback_query_handler(func, lambda s: s.data == "SVAZ_S_RAZRABOTCHIKOM")
    dp.register_message_handler(send_locate, content_types=['location'])


# @dp.message_handler(state=UserState.location, content_types=['location'])
# async def handle_location(message: types.Message, state: FSMContext):
#     user_loc1 = message.location.latitude
#     user_loc2 = message.location.longitude
#     data = await state.get_data()
#     org_loc1 = data['id_in_qr'][0]
#     org_loc2 = data['id_in_qr'][1]
#     res = geolocation.ras(user_loc1, user_loc2, org_loc1, org_loc2)
#     if res > 200 or not res:
#         await message.answer('Вы еще не дошли до работы', reply_markup=types.ReplyKeyboardRemove())
#         await UserState.location.set()
#     else:
#         await message.answer(f'Вы пришли на работу в ', reply_markup=types.ReplyKeyboardRemove())
#         await state.finish()
#     for file in glob.glob(f"data/{message.from_user.id}{message.date}.png"):
#         os.remove(file)

"""

"""
