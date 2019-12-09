from .base_page import BasePage
from .locators import LanguagePageLocators

class LanguagePage(BasePage):
    def change_language(self):
        language_button = self.browser.find_element(*LanguagePageLocators.CHANGE_LANGUAGE_BUTTON)
        language_button.click()
        select_lang_button = self.browser.find_element(*LanguagePageLocators.SELECT_LANGUAGE_BUTTON)
        select_lang_button.click()
        go_button = self.browser.find_element(*LanguagePageLocators.SUBMIT_LANGUAGE_BUTTON)
        go_button.click()

    def should_change_language(self):
        chosen_language_get = self.browser.find_element(*LanguagePageLocators.SUBMIT_LANGUAGE_BUTTON)
        chosen_language = chosen_language_get.text
        assert "Vai" == chosen_language, "Language has not been changed"
