import schedule
import time
import random
import datetime
import subprocess


def is_weekend():
    """Проверка, является ли сегодняшний день выходным."""
    today = datetime.datetime.now().weekday()
    return today >= 5


def run_test(file_path):
    """Запуск теста через subprocess."""
    try:
        subprocess.run(['pytest', '-v', '-s', file_path], check=True)
        print(f'\n{file_path} отработал успешно.')
    except subprocess.CalledProcessError as e:
        print(f'\nОшибка при выполнении {file_path}: {e}')


def schedule_start_day_test():
    """Запланировать выполнение теста из test_bit_start_day_page.py."""
    if is_weekend():
        print("Сегодня выходной. test_bit_start_day_page.py не будет запущен.")
        return

    start_time = datetime.time(hour=8, minute=random.randint(40, 50))
    delay = (datetime.datetime.combine(datetime.date.today(), start_time) - datetime.datetime.now()).total_seconds()

    if delay > 0:
        print(f'\nПохоже, сегодня, ты начнешь вкалывать в {start_time}.')
        time.sleep(delay)
        run_test("test_bit_start_day_page.py")
    else:
        print("Случайное время уже прошло, тест не будет выполнен сегодня.")


def schedule_finish_day_test():
    """Запланировать выполнение теста из test_bit_finish_day_page.py."""
    if is_weekend():
        print("Сегодня выходной. test_bit_finish_day_page.py не будет запущен.")
        return

    finish_time = datetime.time(hour=18, minute=random.randint(0, 10))
    delay = (datetime.datetime.combine(datetime.date.today(), finish_time) - datetime.datetime.now()).total_seconds()

    if delay > 0:
        print(f'\nПохоже, сегодня, ты закончишь вкалывать в {finish_time}.')
        time.sleep(delay)
        run_test("test_bit_finish_day_page.py")
    else:
        print("Случайное время уже прошло, тест не будет выполнен сегодня.")


# Расписание задач
schedule.every().day.at("08:30").do(schedule_start_day_test)
schedule.every().day.at("17:50").do(schedule_finish_day_test)

print('\nСкрипт запущен. '
      '\nЯ попробую проследить, что бы ты не проебался.'
      '\nТеперь ожидай когда я отработаю...')

# Бесконечный цикл для работы schedule
while True:
    schedule.run_pending()
    time.sleep(1)
