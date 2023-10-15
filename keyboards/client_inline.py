from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buttons_for_menu():
    list_for_all_buttons = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('НАЖМИ МЕНЯ', callback_data='CLICK_ME')
    btn2 = InlineKeyboardButton('НАЖМИ МЕНЯ2', callback_data='CLICK_ME2')
    location = InlineKeyboardButton('ОТПРАВИТЬ ЛОКАЦИЮ', callback_data='SEND_LOCATION')
    list_for_all_buttons.add(btn1)
    list_for_all_buttons.add(btn2)
    list_for_all_buttons.add(location)
    return list_for_all_buttons
