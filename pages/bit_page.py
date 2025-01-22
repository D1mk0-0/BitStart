from datetime import datetime

from selenium.webdriver.common.by import By

from .base_page import BasePage

from ..data.preset_data import PresetData

from ..locators.bit_page_locators import BitPageLocators

from ..telegram_logger import setup_telegram_logger

# Настройка логгера
logger = setup_telegram_logger(PresetData.TELEGRAM_BOT_TOKEN, PresetData.TELEGRAM_CHAT_ID)


class BitPage(BasePage):

    def should_be_main_bitrix_mage(self, mine_url):
        self.should_be_main_page_url(mine_url)
        self.should_be_item_time_block()

    def should_be_auth_page(self):
        self.should_be_auth_url()
        self.should_be_title_login_bitrix()
        self.should_be_input_login()
        self.should_be_button_complete()

    def should_be_half_auth_form(self, login):
        self.should_be_title_login_bitrix()
        self.should_be_specified_login_in_form(login)
        self.should_be_input_pass()
        self.should_be_button_complete()

    def should_be_popup_window_with_specified_button(self, button_text):
        self.should_be_window_popup_timeman(button_text)
        self.should_be_specified_button_in_window_popup(button_text)

    def print_successful_message_about_start_day(self):
        successful_message_start_day = \
            ('\nПоздравляю! Трудоголик хуев..'
             f'\nСегодня ты начал свой рабочий день в {self.return_current_time()}')
        print(successful_message_start_day)
        logger.info(successful_message_start_day)

    def print_successful_message_about_finish_day(self):
        successful_message_finish_day = \
            ('\nПоздравляю! Трудоголик хуев..'
             f'\nСегодня ты завершил свой рабочий день в {self.return_current_time()}')
        print(successful_message_finish_day)
        logger.info(successful_message_finish_day)

    def should_be_specified_popup_window_after(self, first_button_text, change_button_text):
        how, what = BitPageLocators.WINDOW_POPUP_TIMEMAN
        button = f'//button[text()="{change_button_text}"]'

        assert self.is_element_present(how, what + button), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            f'\nПосле выбора кнопки ""{first_button_text}"' \
            f'\nНа ее месте должна отобразиться кнопка "{change_button_text}"' \
            '\nА вот ее нет'

    def should_be_item_time_block(self):
        assert self.is_element_present(*BitPageLocators.ITEM_TIME_BLOCK), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            '\nБлок с указанием времени и статусом работы'

    def should_be_auth_url(self):
        assert self.should_be_string_in_url('oauth/authorize'), \
            '\nГде-то мы обосрались:' \
            '\nЗначение элемента отличается от ожидаемого:' \
            '\nСтраница для авторизации не содержит подстроку:' \
            '\noauth/authorize'

    def should_be_main_page_url(self, mine_url):
        assert self.should_be_string_in_url(mine_url), \
            '\nГде-то мы обосрались:' \
            '\nЗначение элемента отличается от ожидаемого:' \
            '\nСтраница для авторизации не содержит подстроку:' \
            f'\n{mine_url}'

    def should_be_button_complete(self):
        assert self.is_element_present(*BitPageLocators.BUTTON_COMPLETE), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            '\nКнопка "Продолжить"'

    def should_be_specified_button_in_window_popup(self, button_text):
        how, what = BitPageLocators.WINDOW_POPUP_TIMEMAN
        button = f'//button[text()="{button_text}"]'

        assert self.is_element_present(how, what + button), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            f'\nКнопка "{button_text}" в попап-окне'

    def select_specified_button_in_window_popup(self, button_text):
        how, what = BitPageLocators.WINDOW_POPUP_TIMEMAN
        button = f'//button[text()="{button_text}"]'
        self.wait_for_present_and_click(how, what + button)

    def select_button_complete(self):
        self.hover_mouse_to_element_and_click(*BitPageLocators.BUTTON_COMPLETE)

    def select_item_time_block(self):
        self.hover_mouse_to_element_and_click(*BitPageLocators.ITEM_TIME_BLOCK)

    def should_be_specified_login_in_form(self, login):
        element = (By.XPATH, '//div[contains(@class, "account-card__user-wrapper")]//div['
                             f'contains(@class, "account-card__login") and text()="{login}"]')
        assert self.is_element_present(*element), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            f'\nУказанный ранее логин на втором шаге авторизации: {login}'

    def should_be_title_login_bitrix(self):
        assert self.is_element_present(*BitPageLocators.TITLE_LOGIN_BITRIX), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            '\nФорма с заголовком "Войти в Битрикс24"'

    def should_be_window_popup_timeman(self, button_text):
        assert self.is_element_present(*BitPageLocators.WINDOW_POPUP_TIMEMAN), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            f'\nПопап-окно с кнопкой "{button_text}"'

    def should_be_input_login(self):
        assert self.is_element_present(*BitPageLocators.INPUT_LOGIN), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            '\nИнпут для заполнения логина'

    def should_be_input_pass(self):
        assert self.is_element_present(*BitPageLocators.INPUT_PASS), \
            '\nГде-то мы обосрались:' \
            '\nЭлемент не был представлен на странице:' \
            '\nИнпут для заполнения пароля'

    def return_current_time(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%H:%M")
        return formatted_date
