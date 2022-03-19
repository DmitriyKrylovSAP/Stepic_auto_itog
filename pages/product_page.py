import math
import pyperclip
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import AddPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*AddPageLocators.PRODUCT_LINK).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            pyperclip.copy(alert_text)
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print(" Не было алерта с задачей")

    def assert_basket(self):
        assert self.is_element_present(*AddPageLocators.SUCSESS_BASKET), "не добавлено в корзину"

    def assert_name(self):
        name = self.browser.find_element(*AddPageLocators.PRODUCT_NAME).text
        name_message = self.browser.find_element(*AddPageLocators.PRODUCT_NAME_MESSAGE).text
        assert name == name_message, "добавлен не тот товар"

    def assert_price(self):
        price = self.browser.find_element(*AddPageLocators.PRODUCT_PRICE).text
        price_message = self.browser.find_element(*AddPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert price == price_message, "не та цена"
