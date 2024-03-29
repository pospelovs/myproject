from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDING_TEXT_WINDOW = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner")
    ADDING_TEXT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE_WINDOW = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[contains(text(), 'View basket')]")
    BASKET_IS_EMPTY = (By.XPATH, "//p[contains(text(), 'empty')]")
    BASKET_HAS_NO_PRODUCT = (By.CSS_SELECTOR, ".btn-block")

class LanguagePageLocators():
    CHANGE_LANGUAGE_BUTTON = (By.NAME, "language")
    SELECT_LANGUAGE_BUTTON = (By.CSS_SELECTOR, "[value='it']")
    SUBMIT_LANGUAGE_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-default[type="submit"]')

class SearchPageLocators():
    SEARCH_FIELD = (By.ID, "id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[value='Search']")
    SEARCH_RESULT_PRODUCT = (By.CSS_SELECTOR, ".product_pod h3 a")

