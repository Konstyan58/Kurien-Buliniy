from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buttons_for_admin():
    list_for_all_buttons = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('РИКРОЛЛ', callback_data='CLICK_ME', url="https://youtu.be/dQw4w9WgXcQ")
    btn2 = InlineKeyboardButton('БАН', callback_data='BAN')
    location = InlineKeyboardButton('ОТПРАВИТЬ ЛОКАЦИЮ', callback_data='SEND_LOCATION')
    list_for_all_buttons.add(btn1)
    list_for_all_buttons.add(btn2)
    list_for_all_buttons.add(location)
    return list_for_all_buttons
