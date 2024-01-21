from aiogram import types, Dispatcher
from config import bot
from keyboards.client_inline import buttons_for_menu, buttons_for_svaz
from pprint import pprint
import requests
from settings import API_TOKEN
from utils.text_utils import s
from handler_db import Database
from states import StateIdea
from aiogram.dispatcher import FSMContext
from keyboards.client_inline import button_for_back
import random

database = Database(pute_k_fily="datas_base/file_dla_chelovekov.db")
photos = ['imgs/1696502279_gas-kvas-com-p-kartinki-lyubie-27.jpg',
          'imgs/a253c5869732a1cbabf74443e1467efd.jpeg',
          'imgs/1e0783c1571e76f71b9bdf2308ffe308.jpeg']
file_idys = ['AgACAgIAAxkBAAIDHWVzDFFRtiGVbnhqJlCq1ExWs-_nAAKjzjEbyEaYSw8NyTtb9MVAAQADAgADeQADMwQ',
             'AgACAgIAAxkBAAIDHmVzDGGG5CN7HNlYzuIfcocgwUHSAAKkzjEbyEaYS1NdHxYrzrnzAQADAgADeQADMwQ',
             'AgACAgIAAxkBAAIDH2VzDG4DK0om553HTUnSu6GBT4srAAKlzjEbyEaYS_zFTGyeVF_cAQADAgADeQADMwQ']
file_idys2 = ["https://prikolnye-kartinki.ru/img/picture/Jun/15/41b89f875a4e9dd7704847adf8a1a8ee/1.jpg"]


async def send_locate(message: types.Message):
    libo_tru_libo_fals_of_ban = await database.check_client_for_ban(nedo_id=message.from_user.id)
    if libo_tru_libo_fals_of_ban == True:
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.send_message(message.from_user.id, 'Вы забанены, если есть вопросы пишите: @The_Steve8')
        return
    cntry, ppltn, temp, vlsnst = s(message.location.latitude, message.location.longitude, API_TOKEN)

    latitude = message.location.latitude
    longituide = message.location.longitude
    await bot.send_message(message.from_user.id, f'Ваши координаты {latitude},{longituide} \n'
                                                 f'Ваша страна (хотя если пользуетесь этим ботом то живёте в СНГ, если конечно бота не перевели): {cntry} \n'
                                                 f'Ваша температура {temp} \n'
                                                 f'Влажность {vlsnst} \n'
                                                 f'AQI {ppltn}')


async def message_text(message: types.Message):
    libo_tru_libo_fals_of_ban = await database.check_client_for_ban(nedo_id=message.from_user.id)
    if libo_tru_libo_fals_of_ban == True:
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.send_message(message.from_user.id, 'Вы забанены, если есть вопросы пишите: @The_Steve8')
        return
    file_iydishnik = message.photo[-1].file_id
    print(file_iydishnik)
    await message.photo[-1].download('img/am.jpg')
    print(message)


async def send_welcome(message: types.Message):
    # await database.crt_new_tbl()
    libo_tru_libo_fals_of_ban = await database.check_client_for_ban(nedo_id=message.from_user.id)
    if libo_tru_libo_fals_of_ban == True:
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.send_message(message.from_user.id, 'Вы забанены, если есть вопросы пишите: @The_Steve8')
        return

    libo_tru_libo_fals = await database.check_client(nedo_id=message.from_user.id)
    if libo_tru_libo_fals == False:
        await database.add_client(nedo_id=message.from_user.id,
                                  frst_or_lst_name=f"{message.from_user.first_name}, {message.from_user.last_name}",
                                  username=message.from_user.username)
    await bot.delete_message(message.from_user.id, message.message_id)

    print(message)
    prinimanie_buttons = buttons_for_menu()
    await bot.send_photo(message.from_user.id, random.choice(file_idys), caption='шото не знаю шо', has_spoiler=False,
                         reply_markup=prinimanie_buttons)


async def func(callback: types.CallbackQuery):
    libo_tru_libo_fals_of_ban = await database.check_client_for_ban(nedo_id=callback.from_user.id)
    if libo_tru_libo_fals_of_ban == True:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_message(callback.from_user.id, 'Вы забанены, если есть вопросы пишите: @The_Steve8')
        return
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    prinimanie_buttons = buttons_for_svaz()
    await bot.send_photo(callback.from_user.id, random.choice(file_idys), caption='шото не знаю шо', has_spoiler=False,
                         reply_markup=prinimanie_buttons)


async def send_something(callback: types.CallbackQuery):
    print(callback)


async def back_to_menu(callback: types.CallbackQuery):
    libo_tru_libo_fals_of_ban = await database.check_client_for_ban(nedo_id=callback.from_user.id)
    if libo_tru_libo_fals_of_ban == True:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_message(callback.from_user.id, 'Вы забанены, если есть вопросы пишите: @The_Steve8')
        return
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    prinimanie_buttons = buttons_for_menu()
    await bot.send_photo(callback.from_user.id, random.choice(file_idys), caption='шото не знаю шо', has_spoiler=False,
                         reply_markup=prinimanie_buttons)


async def idea_handler(callback: types.CallbackQuery):
    libo_tru_libo_fals_of_ban = await database.check_client_for_ban(nedo_id=callback.from_user.id)
    if libo_tru_libo_fals_of_ban == True:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_message(callback.from_user.id, 'Вы забанены, если есть вопросы пишите: @The_Steve8')
        return
    await StateIdea.wait_to_idea.set()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_photo(callback.from_user.id, random.choice(file_idys2), caption='напиши свою идею',
                         has_spoiler=False)


async def sending(message: types.Message, state: FSMContext):
    libo_tru_libo_fals_of_ban = await database.check_client_for_ban(nedo_id=message.from_user.id)
    if libo_tru_libo_fals_of_ban == True:
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.send_message(message.from_user.id, 'Вы забанены, если есть вопросы пишите: @The_Steve8')
        return
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await bot.delete_message(message.from_user.id, message.message_id)
    back = button_for_back()
    await bot.send_message(message.from_user.id, text="Ваше сообщение было отправлено", reply_markup=back)
    await bot.send_message(-1001817158930,
                           f"пользователь {message.from_user.first_name} под ником @{message.from_user.username}, отправил идею: {message.text}")
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(message_text, content_types=['photo'])
    dp.register_message_handler(sending, state=StateIdea.wait_to_idea)
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_callback_query_handler(send_something, lambda s: s.data == "CLICK_ME")
    dp.register_callback_query_handler(func, lambda s: s.data == "SVAZ_S_RAZRABOTCHIKOM")
    dp.register_callback_query_handler(back_to_menu, lambda s: s.data == "BACK")
    dp.register_callback_query_handler(idea_handler, lambda s: s.data == "IDEA")
    dp.register_message_handler(send_locate, content_types=['location'])


"""
1. Сделать систему банов
"""
