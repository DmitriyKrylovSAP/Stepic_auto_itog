from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')

class AddPageLocators:
    PRODUCT_LINK = (By.CSS_SELECTOR, '#add_to_basket_form')
    SUCSESS_BASKET = (By.CSS_SELECTOR, '#messages')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(1) > .alertinner  > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages > :nth-child(3) > .alertinner > p > strong')