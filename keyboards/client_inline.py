from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buttons_for_menu():
    list_for_all_buttons = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton('НАЖМИ МЕНЯ', callback_data='CLICK_ME', url="https://youtu.be/dQw4w9WgXcQ")
    location = InlineKeyboardButton('ОТПРАВИТЬ ЛОКАЦИЮ', callback_data='SEND_LOCATION')
    svaz = InlineKeyboardButton('СВЯЗЬ С РАЗРАБОТЧИКОМ', callback_data='SVAZ_S_RAZRABOTCHIKOM')

    list_for_all_buttons.add(btn1)
    list_for_all_buttons.add(location)
    list_for_all_buttons.add(svaz)

    return list_for_all_buttons


def buttons_for_svaz():
    list_for_all_buttons = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton('ИДЕЯ', callback_data='IDEA')
    btn2 = InlineKeyboardButton('ЖАЛОБА', callback_data='REPORT', url='https://github.com/')
    btn3 = InlineKeyboardButton('ВЕРНУТЬСЯ НАЗАД', callback_data='BACK')
    list_for_all_buttons.add(btn1)
    list_for_all_buttons.add(btn2)
    list_for_all_buttons.add(btn3)

    return list_for_all_buttons


def button_for_back():
    list_for_all_buttons = InlineKeyboardMarkup()
    btn3 = InlineKeyboardButton('ВЕРНУТЬСЯ НАЗАД', callback_data='BACK')
    list_for_all_buttons.add(btn3)

    return list_for_all_buttons
