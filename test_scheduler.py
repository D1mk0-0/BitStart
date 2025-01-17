import schedule
import time
import random
import datetime
import subprocess
from telegram_logger import setup_telegram_logger
from data.preset_data import PresetData

# Настройка логгера
logger = setup_telegram_logger(PresetData.TELEGRAM_BOT_TOKEN, PresetData.TELEGRAM_CHAT_ID)


def is_weekend():
    """Проверка, является ли сегодняшний день выходным."""
    today = datetime.datetime.now().weekday()
    return today >= 5


def run_test(file_path):
    """Запуск теста через subprocess."""
    try:
        run_message = f"\nЗапуск {file_path}."
        logger.info(run_message)
        print(run_message)
        subprocess.run(['pytest', '-v', '-s', file_path], check=True)
        run_ok_message = f'\n{file_path} отработал успешно.'
        logger.info(run_ok_message)
        print(run_ok_message)
    except subprocess.CalledProcessError as e:
        run_error_message = f'\nОшибка при выполнении {file_path}: {e}'
        logger.error(run_error_message)
        print(run_error_message)


def schedule_start_day_test():
    """Запланировать выполнение теста из test_bit_start_day_page.py."""
    if is_weekend():
        start_day_weekend_message = '\nСегодня выходной. Ты, тунеядец, работать не будешь.'
        logger.info(start_day_weekend_message)
        print(start_day_weekend_message)
        return

    start_time = datetime.time(hour=8, minute=random.randint(40, 50))
    delay = (datetime.datetime.combine(datetime.date.today(), start_time) - datetime.datetime.now()).total_seconds()

    if delay > 0:
        start_day_message = f'\nПохоже, сегодня, ты начнешь вкалывать в {start_time}.'
        logger.info(start_day_message)
        print(start_day_message)
        time.sleep(delay)
        run_test("test_bit_start_day_page.py")
    else:
        start_day_error_message = ('\nКажется я где-то проебался..'
                                   '\nПридется тебе начать этот день самому.')
        logger.info(start_day_error_message)
        print(start_day_error_message)


def schedule_finish_day_test():
    """Запланировать выполнение теста из test_bit_finish_day_page.py."""
    if is_weekend():
        finish_day_weekend_message = '\nСегодня выходной. Хотя, ты и без меня то не работал.'
        logger.info(finish_day_weekend_message)
        print(finish_day_weekend_message)
        return

    finish_time = datetime.time(hour=18, minute=random.randint(0, 10))
    delay = (datetime.datetime.combine(datetime.date.today(), finish_time) - datetime.datetime.now()).total_seconds()

    if delay > 0:
        finish_day_message = f'\nПохоже, сегодня, ты закончишь вкалывать в {finish_time}.'
        logger.info(finish_day_message)
        print(finish_day_message)
        time.sleep(delay)
        run_test("test_bit_finish_day_page.py")
    else:
        finish_day_error_message = ('\nКажется я где-то проебался..'
                                    '\nПридется тебе закончить этот день самому.')
        logger.info(finish_day_error_message)
        print(finish_day_error_message)


# Расписание задач
schedule.every().day.at("08:30").do(schedule_start_day_test)
schedule.every().day.at("17:50").do(schedule_finish_day_test)

try:
    start_script_message = ('\nСкрипт запущен.'
                            '\nЯ попробую проследить, что бы ты не проебался.'
                            '\nТеперь ожидай когда я отработаю...')
    logger.info(start_script_message)
    print(start_script_message)
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Программа завершена пользователем.")
