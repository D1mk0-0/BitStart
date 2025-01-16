import pytest

from .data.preset_data import PresetData

from .locators.bit_page_locators import BitPageLocators

from .pages.bit_page import BitPage
from .pages.main_page import MainPage


class TestBitFinishDayPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = MainPage(browser, PresetData.MAIN_BIT_URL)
        page.open()
        self.bit_page = BitPage(browser, browser.current_url)
        self.bit_page.should_be_auth_page()
        self.bit_page.select_clear_and_fill_field_not_enter(
            *BitPageLocators.INPUT_LOGIN, PresetData.LOGIN_BIT
        )
        self.bit_page.select_button_complete()
        self.bit_page.should_be_half_auth_form(PresetData.LOGIN_BIT)
        self.bit_page.select_clear_and_fill_field_not_enter(
            *BitPageLocators.INPUT_PASS, PresetData.LOGIN_PASS
        )
        self.bit_page.select_button_complete()

    def test_finish_bit_day(self, browser):
        self.bit_page.should_be_main_bitrix_mage(PresetData.MAIN_BIT_URL)
        self.bit_page.select_item_time_block()
        self.bit_page.should_be_popup_window_with_specified_button(PresetData.BUTTON_FINISH)
        self.bit_page.select_specified_button_in_window_popup(PresetData.BUTTON_FINISH)
        self.bit_page.should_be_specified_popup_window_after(PresetData.BUTTON_START, PresetData.BUTTON_CONTINUE)
        self.bit_page.print_successful_message_about_finish_day()