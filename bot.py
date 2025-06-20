import os
from aiogram import Bot, Dispatcher, types, executor

# Получаем токен из переменной окружения
API_TOKEN = os.environ["API_TOKEN"]

# Создаем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start — отправляет кнопку
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    button = types.InlineKeyboardButton(text="Жми котик", callback_data="cookie")
    markup = types.InlineKeyboardMarkup().add(button)
    await message.answer("Хочешь печеньку? 🍪", reply_markup=markup)

# Обработка нажатия на кнопку
@dp.callback_query_handler(lambda c: c.data == "cookie")
async def send_cookie(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(
        callback_query.from_user.id,
        photo="https://upload.wikimedia.org/wikipedia/commons/6/69/Chocolate_Chip_Cookies_-_kimberlykv.jpg"
    )
# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
