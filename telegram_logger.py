import logging
from telegram import Bot
from telegram.constants import ParseMode
import asyncio


class TelegramHandler(logging.Handler):
    """Логгер для отправки сообщений в Telegram."""
    def __init__(self, bot_token, chat_id):
        super().__init__()
        self.bot_token = bot_token
        self.chat_id = chat_id

    async def send_message(self, message):
        """Асинхронная отправка сообщения в Telegram."""
        try:
            async with Bot(token=self.bot_token) as bot:
                await bot.send_message(chat_id=self.chat_id, text=message, parse_mode=ParseMode.HTML)
        except Exception as e:
            print(f"Ошибка отправки сообщения в Telegram: {e}")

    def emit(self, record):
        log_entry = self.format(record)
        try:
            loop = asyncio.get_event_loop()
            if not loop.is_running():
                asyncio.run(self.send_message(log_entry))
            else:
                asyncio.ensure_future(self.send_message(log_entry))
        except RuntimeError:
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            try:
                new_loop.run_until_complete(self.send_message(log_entry))
            finally:
                new_loop.close()


def setup_telegram_logger(bot_token, chat_id):
    """Настройка логгера Telegram."""
    logger = logging.getLogger("telegram_logger")
    logger.setLevel(logging.INFO)

    telegram_handler = TelegramHandler(bot_token, chat_id)
    formatter = logging.Formatter('<b>%(levelname)s</b>: %(message)s')
    telegram_handler.setFormatter(formatter)
    logger.addHandler(telegram_handler)

    return logger
