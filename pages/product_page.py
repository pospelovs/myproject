from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        link.click()

    def should_be_basket_page(self):
        self.should_be_adding_message()
        self.should_be_product_name()
        self.should_be_price()

    def should_be_adding_message(self):
        adding_message_get = self.browser.find_element(*ProductPageLocators.ADDING_TEXT_WINDOW)
        adding_message = adding_message_get.text
        assert "has been added to your basket" in adding_message, "There is no special text in pop-up message"

    def should_be_product_name(self):
        adding_message_product_name_get = self.browser.find_element(*ProductPageLocators.ADDING_TEXT_PRODUCT_NAME)
        adding_message_product_name = adding_message_product_name_get.text
        product_name_get = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name_get.text
        assert product_name == adding_message_product_name, "There is no correct product name in pop-up message"

    def should_be_price(self):
        product_price_window_get = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_WINDOW)
        product_price_window = product_price_window_get.text
        product_price_get = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price_get.text
        assert product_price in product_price_window, "Basket price differs from product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING_TEXT_WINDOW), "Success message is presented, but should not be"

    def should_be_disappeared (self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_TEXT_WINDOW), "Success message is not disappeared, but should be"
