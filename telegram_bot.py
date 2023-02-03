from aiogram.utils import executor
from create_bot import *
from handlers import *
from data_base import *

async def on_startup(_):
    print('бот в онлайн')
    sqlite_db.sql_start()

client.register_hendlers_client(dp)
# admin.register_hendlers_admin(dp)

common.register_hendlers_common(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)    