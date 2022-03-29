from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def empty_basket(self):
        self.browser.find_element(*BasketPageLocators.BUTTON_BASKET).click()

    def no_goods (self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Корзина не пуста"
        #print(self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text)

        #self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        #print(self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text)

        #login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link.click()


"""class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK_INVALID), "Login link is not presented"
"""