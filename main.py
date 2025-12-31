import asyncio
from aiogram import Dispatcher, filters, Bot
from aiogram.types import message
dp = Dispatcher()
@dp.message(filters.CommandStart())
async def start (message: message ):
  await message.answer(
      text= "hey you"
  )

async def main():
    bot = Bot (token="7917494954:AAFB_t33laIFy428T8SjsTNv0OIzNAfjusI")
    await dp.start_polling(bot) 
    
    
if __name__== "__main__" :
     asyncio.run(main())