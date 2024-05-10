import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
async def main():
    bot = Bot(token='7066986752:AAFA7SZEtNwvKOHWaChTs5ZMxTtLDj-UGt4')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")