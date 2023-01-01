from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from New_life_3.config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from New_life_3.handler import dp
    executor.start_polling(dp, skip_updates=True)
