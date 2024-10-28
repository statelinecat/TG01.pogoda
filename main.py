import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Я умею выполнять команды:\\n/start\\n/help")
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())