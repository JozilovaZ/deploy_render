from aiogram import Router,types
from aiogram.filters import Command
from filters.fillters import IsAdmin
ur=Router()


@ur.message(Command("start"),IsAdmin())
async def start(message:types.Message):
    await message.reply("Salom admin botimizga xush kelibsiz")  

@ur.message(Command("start"))
async def start(message:types.Message):
    await message.reply("Assalomu alaykum")



  
