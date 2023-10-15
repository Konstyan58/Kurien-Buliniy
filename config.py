from aiogram import Bot, Dispatcher
from settings import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)    # диспетчер - помогает понять, что отправили (фотку, запрос какой-нибудь, видео/аудио...)
