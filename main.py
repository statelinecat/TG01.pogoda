import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=TOKEN)
# storage = MemoryStorage()  # Добавим хранилище
dp = Dispatcher()

@dp.message(F.text == 'Привет!')
async def hitext(message: Message):
    await message.answer("Привет! Я сообщаю информацию о погоде. Также умею выполнять команды: \n /start \n /help")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Я умею выполнять команды: \n /start \n /help")
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())