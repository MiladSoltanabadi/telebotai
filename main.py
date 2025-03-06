import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from transformers import pipeline
import os

# Telegram Token
API_TOKEN = 'Bot Token'

# Log Settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loading Model

os.environ["TRANSFORMERS_CACHE"] = "path/to/cache/directory"  # if you don't want that the model goes to C drive

MODEL_NAME = "HooshvareLab/gpt2-fa"
logger.info("در حال بارگیری مدل زبان فارسی...")
try:
    text_generator = pipeline("text-generation", model=MODEL_NAME)
    logger.info("مدل زبان فارسی با موفقیت بارگیری شد.")
except Exception as e:
    logger.error(f"خطا در بارگیری مدل: {e}")
    raise

# Telegram bot Settings
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Bot Starter
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"کاربر {message.from_user.id} دستور /start را ارسال کرد.")
    await message.answer("سلام! من چت‌بات هوشمند هستم. هر پیامی بفرستید تا پاسخ دهم.")


# Bot(AI) respond
@dp.message()
async def ai_chat(message: types.Message):
    user_input = message.text
    logger.info(f"کاربر {message.from_user.id} پیام ارسال کرد: {user_input}")

    # Show Process Statue
    '''If you don't want it you can remove or comment this section'''
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")

    try:
        logger.info("در حال تولید پاسخ با مدل زبان فارسی...")
        # Creating respond(you can change here for your needs)
        output = text_generator(user_input, max_length=100, num_return_sequences=1, do_sample=True, temperature=0.7)
        response = output[0]['generated_text']

        if response.startswith(user_input):
            response = response[len(user_input):].strip()
        logger.info(f"پاسخ تولید شده: {response}")
    except Exception as e:
        logger.error(f"خطا در تولید پاسخ: {e}")
        response = "مشکلی در تولید پاسخ پیش آمده. لطفاً دوباره امتحان کنید."

    await message.answer(response)


# Run bot
async def main():
    logger.info("ربات در حال راه‌اندازی است...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
