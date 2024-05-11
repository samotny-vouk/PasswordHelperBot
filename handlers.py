from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import keyboard as kb
from functions import password, check_password


f_start = open('start_message.txt', encoding='utf-8')
f_about = open('about.txt', encoding='utf-8')
f_adv = open('advices.txt', encoding='utf-8')

start_msg = f_start.read()
about = f_about.read()
adv = f_adv.read()

users_password = State()

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(start_msg, reply_markup=kb.main )

@router.message(F.text == 'Перезапустить')
async def cmd_start(message: Message):
    await message.answer(start_msg, reply_markup=kb.main )


@router.message(Command('about'))
async def cmd_help(message: Message):
    await message.answer(about)

@router.message(F.text == 'О боте PasswordHelper')
async def cmd_help(message: Message):
    await message.answer(about)


@router.message(Command('menu'))
async def cmd_help(message: Message):
    await message.answer("Выберите функцию", reply_markup=kb.menu)

@router.message(F.text == 'Меню функций')
async def cmd_help(message: Message):
    await message.answer("Выберите функцию", reply_markup=kb.menu)


@router.callback_query(F.data == 'password')
async def t_shirt(callback: CallbackQuery):
    await callback.message.answer('Ваш пароль готов: ' + password())


@router.callback_query(F.data == 'check')
async def t_shirt(callback: CallbackQuery, state: FSMContext):
    await state.set_state(users_password)
    await callback.message.answer('Введите ваш пароль')

@router.message(users_password)
async def register(message: Message, state: FSMContext):
    await state.update_data(users_password=message.text)
    await message.answer(check_password(message.text))


@router.callback_query(F.data == 'advices')
async def t_shirt(callback: CallbackQuery):
    await callback.message.answer(adv)


f_start.close()
f_about.close()
f_adv.close()