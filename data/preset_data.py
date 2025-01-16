from dotenv import load_dotenv
import os


class PresetData:
    load_dotenv()
    MAIN_BIT_URL = os.getenv('MAIN_BIT_URL', '')
    LOGIN_BIT = os.getenv('LOGIN_BIT', '')
    LOGIN_PASS = os.getenv('LOGIN_PASS', '')

    BUTTON_START = os.getenv('BUTTON_START', '')
    BUTTON_FINISH = os.getenv('BUTTON_FINISH', '')
    BUTTON_CONTINUE = os.getenv('BUTTON_CONTINUE', '')

    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')


