import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8349584164:AAHMS-RarqdJdntec03FzXUlW3r_J6hORZI"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    text = (
        "Salom! Men Viktorina (Quiz) botman 🧠\n\n"
        "Bilimingizni sinash uchun /quiz buyrug'ini yuboring!"
    )
    await message.answer(text)

@dp.message(Command("quiz"))
async def quiz_cmd(message: types.Message):
    question = (
        "<b>Savol:</b> Python dasturlash tili qaysi yilda yaratilgan?\n\n"
        "A) 1989\n"
        "B) 1995\n"
        "C) 2000\n\n"
        "Javob berish uchun quyidagi buyruqlardan birini bosing:\n"
        "/answer_a — A varianti\n"
        "/answer_b — B varianti\n"
        "/answer_c — C varianti"
    )
    await message.answer(question, parse_mode="HTML")

@dp.message(Command("answer_a"))
async def correct_answer(message: types.Message):
    await message.answer("To'g'ri! 🎉 Python 1989-yilda Guido van Rossum tomonidan yaratilgan.")

@dp.message(Command("answer_b"))
async def wrong_b(message: types.Message):
    await message.answer("Afsus, noto'g'ri ❌ To'g'ri javob A varianti (1989-yil) edi.")

@dp.message(Command("answer_c"))
async def wrong_c(message: types.Message):
    await message.answer("Afsus, noto'g'ri ❌ To'g'ri javob A varianti (1989-yil) edi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())