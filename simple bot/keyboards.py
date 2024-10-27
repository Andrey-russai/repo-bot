from aiogram import types


button1 = types.KeyboardButton(text='/cmd')
button2 = types.KeyboardButton(text='/start')
button3 = types.KeyboardButton(text='вход')
button4 = types.KeyboardButton(text='выход')
button5 = types.KeyboardButton(text='Покажи Лису')


#коллекция данных, список, значения
keyboard1 = [
    [button1, button2, button3],
    [button4, button5]
]


keyboard2 = [
    [button3, button4],
    [button5]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

