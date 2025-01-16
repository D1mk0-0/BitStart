from selenium.webdriver.common.by import By


class BitPageLocators:
    TITLE_LOGIN_BITRIX = (By.XPATH, '//div/h2[text()="Войти в Битрикс24"]')

    INPUT_LOGIN = (By.XPATH, '//input[@id="login"]')
    INPUT_PASS = (By.XPATH, '//input[@type="password"]')

    BUTTON_COMPLETE = (By.XPATH, '//button/span[text()="Продолжить"]')

    ITEM_TIME_BLOCK = (By.XPATH, '//div[@id="timeman-container"]')

    WINDOW_POPUP_TIMEMAN = (By.XPATH, '//div[@class="popup-window --open" and @id="timeman_main"]')
