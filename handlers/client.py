from aiogram import types, Dispatcher
from config import bot
from keyboards.client_inline import buttons_for_menu
from pprint import pprint
import requests
from settings import API_TOKEN
from utils.text_utils import s


async def send_locate(message: types.Message):
    cntry, ppltn, temp, vlsnst = s(message.location.latitude, message.location.longitude, API_TOKEN)
    latitude = message.location.latitude
    longituide = message.location.longitude
    await bot.send_message(message.from_user.id, f'Ваши координаты {latitude},{longituide} \n'
                                                 f'Ваша страна (хотя если пользуетесь этим ботом то живёте в СНГ, если конечно бота не перевели): {cntry} \n'
                                                 f'Ваша температура {temp} \n'
                                                 f'Влажность {vlsnst} \n'
                                                 f'AQI {ppltn}')


async def send_welcome(message: types.Message):
    print(message)
    prinimanie_buttons = buttons_for_menu()
    await bot.send_message(message.from_user.id, 'ъуъ', reply_markup=prinimanie_buttons)


async def send_something(callback: types.CallbackQuery):
    print(callback)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_callback_query_handler(send_something, lambda s: s.data == "CLICK_ME")
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
1. Загуглить: "как создать keyboard кпноку для получения локации aiogram python"
2. Загуглить: "как получить и обработать локацию в aiogram python"
3. Создать новую кнопку с "Отправить локацию" (как-то так😁)
4. Обработать её и зарегистрировать
5.зарегаться на глифе
"""
