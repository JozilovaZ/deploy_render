import asyncio
import logging
from loader import bot, dp
from aiogram import Router
from heanler import set_up
from middleweres.throttling import ThrottlingMiddlewere


async def main()->None:
   main_router=set_up()
   dp.include_router(main_router)


   dp.message.middleware(ThrottlingMiddlewere(slow_mode_delay=3))


   logging.info("Bot ishladi")
   await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)    
    asyncio.run(main())
    