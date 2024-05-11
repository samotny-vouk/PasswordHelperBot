from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Меню функций')],
                                     [KeyboardButton(text='О боте PasswordHelper')],
                                     [KeyboardButton(text='Перезапустить')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пунтк меню...')

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Генератор паролей', callback_data='password')],
    [InlineKeyboardButton(text='Проверить пароль на надежность', callback_data='check')],
    [InlineKeyboardButton(text='Как выбрать пароль?', callback_data='advices')]])