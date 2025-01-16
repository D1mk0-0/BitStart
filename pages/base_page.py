import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_text_of_element(self, how, what):
        """Возвращает текст из элемента."""
        text_of_element = self.browser.find_element(how, what).get_attribute('textContent')
        return text_of_element

    def get_attribute_value_of_element(self, how, what, attribute_name):
        """Возвращает значение указанного атрибута элемента."""
        attribute_value_of_element = self.browser.find_element(how, what).get_attribute(f'{attribute_name}')
        return attribute_value_of_element

    def get_text_of_elements(self, how, what):
        """Возвращает текст из ВСЕХ элементов."""
        elements = self.browser.find_elements(how, what)
        text_of_elements = [element.get_attribute('textContent') for element in elements]
        return text_of_elements

    def get_href_of_element(self, how, what):
        """Возвращает ссылку из элемента."""
        href_of_element = self.browser.find_element(how, what).get_attribute('href')
        return href_of_element

    def hover_mouse_to_element_and_click(self, how, what):
        """Наводит курсор на элемент."""
        hoverable = self.browser.find_element(how, what)
        ActionChains(self.browser) \
            .move_to_element(hoverable) \
            .click(hoverable) \
            .perform()

    def is_element_present(self, how, what, timeout=20):
        """Представлен ли элемент на странице."""
        time.sleep(.2)
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=10):
        """Элемент отсутствует на странице."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Элемент должен исчезнуть."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def refresh(self):
        self.browser.refresh()

    def select_clear_and_fill_field_not_enter(self, how, what, input_value):
        """Выбирает, очищает и заполняет поле не нажимая ENTER."""
        self.wait_is_element_clickable_and_click(how, what)
        input_data = self.browser.find_element(how, what)
        input_data.clear()
        input_data.send_keys(input_value)

    def should_be_string_in_url(self, url_str, timeout=10):
        """Ожидает пока url не будет содержать указанную подстроку."""
        try:
            wait = WebDriverWait(self.browser, timeout)
            wait.until(EC.url_contains(url_str))
            return True
        except TimeoutException:
            return False

    def page_loaded(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_all_elements_located)

    def page_visible(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_all_elements_located)

    def wait_for_present_and_click(self, how, what, timeout=10):
        time.sleep(.5)
        if self.is_element_present(how, what, timeout):
            self.browser.find_element(how, what).click()
        else:
            assert False, f'Элемент с локатором {how, what} не был найден на станице'

    def wait_is_element_clickable_and_click(self, how, what, timeout=10):
        """Будет обращаться к элементу, пока он не станет доступен."""
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
            element.click()
        except TimeoutException:
            return False
        return True
