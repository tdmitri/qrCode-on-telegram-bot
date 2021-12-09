from aiogram import Bot, Dispatcher, types, executor
import pyqrcode as pq
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def starter(msg: types.Message):
    await msg.answer('Привет,\nПришли мне любой текст и я сделаю из него QR код.\nДля этого используй команду /text')


@dp.message_handler(commands=['text'])
async def send_text_based_qr(msg: types.Message):
    await msg.answer('Ваш текст принят на обработку.\nПожалуйста подождите!')

    qr_code = pq.create(msg.text)
    qr_code.png('code.png', scale=6)

    with open('code.png', 'rb') as photo:
        await bot.send_photo(msg.chat.id, photo)
        await bot.send_message(msg.chat.id, 'QR код готов, Вы можете прислать новый текст.')

executor.start_polling(dp)
