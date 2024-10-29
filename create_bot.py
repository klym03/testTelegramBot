from aiogram import Bot
from dotenv.main import load_dotenv
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Initialize bot and dispatcher
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


load_dotenv()
storage = MemoryStorage()
tkn = os.environ['TOKEN']
bot = Bot(token=tkn, default=DefaultBotProperties(parse_mode=ParseMode.HTML))