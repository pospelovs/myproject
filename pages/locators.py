from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDING_TEXT_WINDOW = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner")
    ADDING_TEXT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE_WINDOW = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[contains(text(), 'View basket')]")
    BASKET_IS_EMPTY = (By.XPATH, "//p[contains(text(), 'empty')]")
    BASKET_HAS_NO_PRODUCT = (By.CSS_SELECTOR, ".btn-block")
