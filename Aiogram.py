from aiogram import Bot, Dispatcher, executor, types
import time
import logging
import asyncio
from config import TOKEN as API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
MSG = "Здарова мухомор {}!"


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')

    await message.reply(f"Привет, {user_full_name}!")

    await asyncio.sleep(1)
    await bot.send_message(user_id, MSG.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)