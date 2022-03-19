from selenium import webdriver
import math
import pyperclip

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
browser.find_element_by_id("add_to_basket_form").click()

alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
pyperclip.copy(answer)
pyperclip.paste()




