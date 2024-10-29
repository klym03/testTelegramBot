import asyncio
from create_bot import bot, dp
from handlers.client import router

async def start():
    # client.register_handlers_client(dp)  # Реєстрація обробників
    print('bot is online')
    dp.include_routers(
        router,
    )
    await dp.start_polling(bot, skip_updates=True)  # Запуск опитування

if __name__ == '__main__':
    asyncio.run(start())
