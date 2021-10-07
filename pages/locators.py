from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	
class ProductPageLocators():
    ADD_CART_BTN = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    TEXT_IN_MSG = (By.CSS_SELECTOR, "[contains(text(), ' был добавлен в вашу корзину.')]")
    NAME_PRODUCT_IN_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")