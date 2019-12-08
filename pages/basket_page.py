from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_page(self):
        self.should_be_empty_message()
        self.should_not_be_products()

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty"

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAS_NO_PRODUCT), "There is products in the basket"
