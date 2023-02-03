from aiogram import types, Dispatcher
from create_bot import *
# import json, string


# @dp.message_handler()
async def echo(message: types.Message):
            await message.reply("Унда шу ботга кириб start тугмасини босинг \nhttps://t.me/bot_AladdinBot \n ва кегин '/мыть' деб йозинг")

    # if {i.lower().translate(str.maketrans('', '', string.punctuation))for i in message.text.split(' ')}\
    #     .intersection(set(json.load(open('filtre_mat.json')))) != set():
    #     await message.reply('в этом группе маты запрешены')
    #     await message.delete()


def register_hendlers_common(dp: Dispatcher):
    dp.register_message_handler(echo, lambda message: 'гилам ювдирмокчиман' or 'gilam yuvdirmokchiman' in message.text)