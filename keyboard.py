from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')
catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='футболка', callback_data='t-shirt')],
    [InlineKeyboardButton(text='кепка', callback_data='cap')],
    [InlineKeyboardButton(text='джинсы', callback_data='jeans')]])