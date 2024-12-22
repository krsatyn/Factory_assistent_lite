# bot id @factory_sgau_bot

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message



start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Здравстуйте, я языковая модель, предназначенная для помощи на производстве. Для помощи напишите /help')
    
@start_router.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer('Что бы пользоваться ботом, просто напишите свой запрос, далее бот попробует вам помочь')
    
@start_router.message(F.text == 'filter')
async def cmd_start(message: Message):
    await message.answer('проверка /filter, magic filter = F.text')