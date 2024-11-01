import logging
import asyncio
from random import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from keyboards import kb1, kb2
from random_fox import fox


API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("cmd"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет, {name}", reply_markup=kb1)


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(f"Hello")


@dp.message(Command("continue"))
async def command_continue(message: types.Message):
    await message.answer(f"Good!")


@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(Command("лису"))
@dp.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Держи Лису, {name}!")
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)


@dp.message(Command("ваше_имя"))
async def send_username(message: types.Message):
    await message.answer(f"admin")


@dp.message(Command("вход"))
async def send_enter(message: types.Message):
    await message.answer(f"выполнен")


@dp.message(Command("вход"))
async def send_enter(message: types.Message):
    await message.answer(f"выполнен")

@dp.message(Command("выход"))
async def send_exit(message: types.Message):
    await message.answer(f"выполняется")


@dp.message(F.text)
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


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    