
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# def kb_client() -> ReplyKeyboardMarkup:
#     start_button = KeyboardButton('/start')
#     return kb_client

def ikb_client_main_menu(goods_list, row_width=1):
    builder = InlineKeyboardBuilder()
    for good in goods_list:
        builder.add(InlineKeyboardButton(text=good, callback_data=f'good_{good}'))
    builder.adjust(row_width)
    return builder
def back_to_main_menu():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Повернутися до головного меню', callback_data='back_to_main_menu'))
    return builder


