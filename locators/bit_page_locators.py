from selenium.webdriver.common.by import By


class BitPageLocators:
    TITLE_LOGIN_BITRIX = (By.XPATH, '//div/h2[text()="Войти в Битрикс24"]')

    INPUT_LOGIN = (By.XPATH, '//input[@id="login"]')
    INPUT_PASS = (By.XPATH, '//input[@type="password"]')

    BUTTON_COMPLETE = (By.XPATH, '//button/span[text()="Продолжить"]')

    USER_AVATAR = (By.XPATH, '//div[contains(@class,"air-user-profile__avatar")]')

    ITEM_TIME_BLOCK = (By.XPATH, '//div[@id="timeman-container"]')

    WINDOW_POPUP_TIMEMAN = (By.XPATH, '//div[@id="popup-window-content-timeman_main"]')
    WINDOW_POPUP_AVATAR_HEADER = (By.XPATH, '//div[@id="bx-avatar-header-popup"]')
