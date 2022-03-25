from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1, "Login url not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ELEMENT), "Email element is not presented"
        emailElement = self.browser.find_element(*LoginPageLocators.EMAIL_ELEMENT)
        emailElement.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.PASSWORD_ELEMENT), "Password element is not presented"
        passwordElement = self.browser.find_element(*LoginPageLocators.PASSWORD_ELEMENT)
        passwordElement.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.CONFIRM_ELEMENT), "Confirm element is not presented"
        confirmElement = self.browser.find_element(*LoginPageLocators.CONFIRM_ELEMENT)
        confirmElement.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
        registerButton = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registerButton.click()

