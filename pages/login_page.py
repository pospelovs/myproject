from .base_page import BasePage
from .locators import LoginPageLocators
import time

def register_new_user(self, email, password):
    email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
    password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD1)
    password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD2)
    email_input.send_keys(email)
    password1_input.send_keys(password)
    password2_input.send_keys(password)
    button_submit = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
    button_submit.click()

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no login in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "There is no registration form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_submit.click()
