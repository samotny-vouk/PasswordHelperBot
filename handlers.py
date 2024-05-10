from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import keyboard as kb
router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main )
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("помощь")

@router.message(F.text == 'Каталог')
async def cmd_help(message: Message):
    await message.answer("выберите категорию товара", reply_markup=kb.catalog)

@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию', show_alert=True)
    await callback.message.answer('Вы выбрали категорию футболки')

@router.callback_query(F.data == 'jeans')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию джинсы')

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')

@router.message(Register.age)
async def register(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Введите ваш номер телефона')

@router.message(Register.number)
async def register(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await state.clear()