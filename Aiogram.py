import os

from aiogram import Bot, Dispatcher, executor, types
import time
import logging
from asyncio import sleep
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

res = load_dotenv('venv\.env')
if res:
    print('yep')
else:
    print('no')
bot = Bot(os.environ['BOT_TOKEN'])
dp = Dispatcher(bot)
MSG = "Хочешь скипнуть пары, но не уверен?) Тогда отправь мне /dice и мы решим это вместе, {}!"


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    print(message)
    if (message.text == '/start'):
        await message.reply(f"Привет, {message.from_user.full_name}!")

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    print(f'{user_id} {user_full_name} {time.asctime()}')

    await bot.send_message(user_id, MSG.format(user_name))


@dp.message_handler(commands=['dice'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    bot_data = await bot.send_dice(user_id)
    # print(bot_data['dice']['value'])
    bot_data = bot_data['dice']['value']

    await sleep(1)
    user_data = await bot.send_dice(user_id)
    user_data = user_data['dice']['value']

    await sleep(1)
    if bot_data > user_data:
        await bot.send_message(user_id, 'ИДИ НА ПАРЫ, ЛУЗЕР!')
    else:
        await bot.send_message(user_id, 'ЮХУУУУ ВАЛИМ НАХЕР!')
    pass


if __name__ == '__main__':
    executor.start_polling(dp)
