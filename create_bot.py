from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

TOKEN = '5779972313:AAGiBxCWFa7Yt-BZEFVWZ-IHPYfcoiPAt-U'

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)