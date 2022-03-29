from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "have't login in url"
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Reg form is not presented"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_SUBMIT).click()


