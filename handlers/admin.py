# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types, Dispatcher
# from create_bot import *
# from aiogram.dispatcher.filters import Text
# from data_base import sqlite_db
# from keyboards.admin_kb import kb_admin

# class FSM_admin(StatesGroup):
#     name = State()
#     phone = State()
#     address = State()


# @dp.message_handler(commands='мыть')
# async def Order(message: types.Message):
#     await bot.send_message(message.from_user.id, 'ассалому алейкум бизи гилам ювиш фабрикамизи танглаганиздан хурсандмиз ', reply_markup=kb_admin)
#     await message.delete()


# # @dp.message_handler(commands='заказать', state = None)
# async def order_start(message: types.Message):
#     await FSM_admin.name.set()
#     await message.reply('напишите имя')


# # @dp.message_handler(state="*", commands='отмена')
# # @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
# async def cancle_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return None
#     await state.finish()
#     await message.reply('заказ отменен')


# # @dp.message_handler(state=FSM_admin.name)
# async def load_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await FSM_admin.next()
#     await message.reply('теперь напишите номер телефона')


# # @dp.message_handler(state=FSM_admin.phone)
# async def load_phone(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['phone'] = message.text
#     await FSM_admin.next()
#     await message.reply('теперь ведите адресс')


# # @dp.message_handler(state=FSM_admin.address)
# async def load_address(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['address'] = message.text
#     await sqlite_db.sql_add_command(state)
#     await message.reply('заказингиз кабул килинди')
#     await state.finish()



# def register_hendlers_admin(dp: Dispatcher):
#     dp.register_message_handler(order_start, commands=['заказать'], state=None)
#     dp.register_message_handler(cancle_handler, state="*", commands='отмена')
#     dp.register_message_handler(cancle_handler, Text(equals='отмена', ignore_case=True), state="*")
#     dp.register_message_handler(load_name, state=FSM_admin.name)    
#     dp.register_message_handler(load_phone, state=FSM_admin.phone)    
#     dp.register_message_handler(load_address, state=FSM_admin.address)