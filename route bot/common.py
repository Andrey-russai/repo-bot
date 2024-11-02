from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards import kb1, kb2
from random_fox import fox
from random import randint


router = Router()


@router.message(Command("cmd"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет, {name}", reply_markup=kb1)


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(f"Hello")


@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(Command("лису"))
@router.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Держи Лису, {name}!")
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)


@router.message(Command("вход"))
async def send_enter(message: types.Message):
    await message.answer(f"выполнен")

@router.message(Command("выход"))
async def send_exit(message: types.Message):
    await message.answer(f"выполняется")

@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")


@router.message(F.text)
async def echo(message: types.Message):
    if "ура" in message.text.lower():
        await message.answer(F"Good!")
    elif message.text == "инфо":

        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)


@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f"Привет-привет, {name}!")
    elif 'пока' == msg_user:
        await message.answer(f"Пока-пока, {name}!")
    elif 'ты кто?' in msg_user:
        await message.answer_dice(emoji="🦊")
    elif 'вход' in msg_user:
        await message.answer(f"выполнен")
    elif 'выход' in msg_user:
        await message.answer(f"выполняется")
    elif 'лису' in msg_user:
        await message.answer(f"Смотри, что у меня есть, {name}!", reply_markup=kb2)
    else:
        await message.answer(f"Я не знаю такого слова ( ")

