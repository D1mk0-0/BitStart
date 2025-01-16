import logging
from telegram import Bot
import asyncio

from data.preset_data import PresetData


class TelegramHandler(logging.Handler):
    """Логгер для отправки сообщений в Telegram."""
    def __init__(self, bot_token, chat_id):
        super().__init__()
        self.bot = Bot(token=bot_token)
        self.chat_id = chat_id

    async def send_message(self, message):
        """Асинхронная отправка сообщения в Telegram."""
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message)
        except Exception as e:
            print(f"Ошибка отправки сообщения в Telegram: {e}")

    def emit(self, record):
        log_entry = self.format(record)
        asyncio.run(self.send_message(log_entry))


def setup_telegram_logger():
    logger = logging.getLogger("telegram_logger")
    logger.setLevel(logging.INFO)

    telegram_handler = TelegramHandler(PresetData.TELEGRAM_BOT_TOKEN, PresetData.TELEGRAM_CHAT_ID)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    telegram_handler.setFormatter(formatter)
    logger.addHandler(telegram_handler)

    return logger
