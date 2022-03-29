from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    LOGIN_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    LOGIN_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    BTN_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration_submit']")

class AddPageLocators:
    PRODUCT_LINK = (By.CSS_SELECTOR, '#add_to_basket_form')
    SUCSESS_BASKET = (By.CSS_SELECTOR, '#messages')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(1) > .alertinner  > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(3) > .alertinner > p > strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, '.btn-group')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
