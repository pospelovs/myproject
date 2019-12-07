from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

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
        assert "has been added to your basket" in adding_message, "There is no product name in pop-up message"

    def should_be_product_name(self):
        adding_message_get = self.browser.find_element(*ProductPageLocators.ADDING_TEXT_WINDOW)
        adding_message = adding_message_get.text
        product_name_get = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name_get.text
        assert product_name in adding_message, "There is no product name in message"

    def should_be_price(self):
        product_price_window_get = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_WINDOW)
        product_price_window = product_price_window_get.text
        product_price_get = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price_get.text
        assert product_price in product_price_window, "Basket price differs with product price"
