from .base_page import BasePage
from .locators import SearchPageLocators

class SearchPage(BasePage):
    def go_to_search_products(self):
        search_input = self.browser.find_element(*SearchPageLocators.SEARCH_FIELD)
        search_input.send_keys("Work")
        go_search = self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON)
        go_search.click()

    def should_search_products(self):
        search_results_get = self.browser.find_element(*SearchPageLocators.SEARCH_RESULT_PRODUCT)
        search_results = search_results_get.text
        assert "Work" in search_results, "Search does not work correctly"
