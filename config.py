from aiogram import Bot, Dispatcher
from settings import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,
                storage=MemoryStorage())  # диспетчер - помогает понять, что отправили (фотку, запрос какой-нибудь, видео/аудио...)
