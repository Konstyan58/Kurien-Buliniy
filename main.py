from aiogram import executor
from config import dp
from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_client(dp)


async def start_bot(_):
    print('Bot is online ->', _)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
