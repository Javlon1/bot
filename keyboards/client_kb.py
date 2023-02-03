from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


c1 = KeyboardButton('/help')
# c2 = KeyboardButton('поделится номера', request_contact=True)
# c3 = KeyboardButton('отправить где я', request_location=True)

a1 = KeyboardButton('/гилам ювдирмокчиман')
a2 = KeyboardButton('/отмена')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# add, row, insert

kb_client.add(c1).row(a1, a2)#.row(c2, c3)