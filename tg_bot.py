import logging
from random import randint

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import Bot, Dispatcher, executor, types
from flask import request
from flask_restful import Resource
from requests import get, put, post

API_TOKEN = '5305383108:AAFZkZajF_hA03HshrF5-mPnkyTY77caui0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup(one_time_keyboard=True)
keyboard.add(InlineKeyboardButton(text="Заказ готов!", callback_data="ready"))

keyboard2 = InlineKeyboardMarkup(one_time_keyboard=True)
keyboard2.add(InlineKeyboardButton(text="Готово!✅", callback_data="finished"))

keyboard1 = InlineKeyboardMarkup()
keyboard1.add(InlineKeyboardButton(text="To order", callback_data="order"))


@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Начнем работу!", reply_markup=keyboard1)


@dp.callback_query_handler(text="order")
async def send_random_value(call: types.CallbackQuery):
    await bot.send_message(-1001506674517,
                           f'Номер заказа: 2\nИмя клиента: Кирилл\nСодержание заказа:\nЭспрессо(1шт.)\nКруассаны(3шт.)',
                           reply_markup=keyboard)


@dp.callback_query_handler(text="ready")
async def send_random_value(call: types.CallbackQuery):
    a = call.message.text.split('\n')
    num = int(a[0].split()[2])
    put('http://localhost:5000/todo1', data={'data': num}).json()
    await bot.delete_message(chat_id=-1001506674517, message_id=call.message.message_id)
    await bot.send_message(-1001506674517,
                           f'Номер заказа: 2\nИмя клиента: Кирилл\nСодержание заказа:\nЭспрессо(1шт.)\nКруассаны(3шт.)',
                           reply_markup=keyboard2)


def send_mess():
    API_TOKEN = '5305383108:AAFZkZajF_hA03HshrF5-mPnkyTY77caui0'

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Initialize bot and dispatcher
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    bot.send_message(-1001650800039, 'Через другой файл!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
